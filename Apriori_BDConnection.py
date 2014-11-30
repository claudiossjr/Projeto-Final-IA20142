from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb
import ast
from JoinFile1 import Util,HelpTools

util = Util()

helptools = HelpTools()

numberOfTransactions = 0
suport = 0.3
transactions = -1
cursor = -1

def dbConnection():

    #connect to DB

    global cursor

    #print "Insert hostname"
    host = "localhost"#raw_input()
    #print "Insert Username"
    username = "joao" #raw_input()
    #print "Insert your password"
    password = "1234" #raw_input()
    #print "Insert Database"
    database = "teste" #raw_input()

    db = MySQLdb.connect(host, username, password, database)
    cursor = db.cursor()


def checkTransactions():

    #check transactions made for each client

    global cursor
    global transactions

    cursor.execute("SELECT COUNT(DISTINCT idCliente) FROM Compra")
    numberOfTransactions = int(cursor.fetchone()[0])

    transactions = [[] for i in range(numberOfTransactions)]

    cursor.execute("SELECT * FROM Compra")
    auxtransactions = cursor.fetchall()

    for tuple in auxtransactions:
       transactions[int(tuple[1])-1].append(int(tuple[0]))


    # print de cada transacao
    print "TRANSACTIONS"
    for item in transactions:
        print item


    transactions = map(set, transactions)


def buildC1():

    global transactions

    C1 = {}


    for ID in transactions:
        for product in ID:
            if not C1.has_key(product): C1[product] = 1
            else: C1[product] += 1

    '''
    # print do C1. {idProduto, Quantidade}
    for item in C1:
        print " Item: %s Quantidade %s " % (item ,C1[item])
    '''


    L1 = {}

    for item in C1:
        if (float(C1[item]) / float(len(transactions))) > suport:
            L1[item] = C1[item]


            cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(item))
            productName = cursor.fetchall()


            print "%s -----> Suporte: %s " % (productName[0][0], float(C1[item]) / float(len(transactions)))


    L1FINAL = [0 for i in range(len(L1))]


    i = 0
    for item in L1:
        L1FINAL[i] = [item]
        i += 1


    return L1FINAL



def buildLK(LK):



    global transactions,cursor

    CK = util.makeJoins(LK)

    CK = map(set, CK)

    LK = {}



    for itemset in CK:
        aux = map(list,[itemset])
        aux = str(aux)
        temp = ast.literal_eval(aux)
        LK[str(temp[0])] = 0


    for itemset in CK:
        for transaction in transactions:
            if itemset.issubset(transaction):
                temp = map(list,[itemset])
                LK[str(temp[0])] +=1


    LKFINAL = []

    for item in LK:
        if (float(LK[item])/float(len(transactions))) > suport:

            temp = ast.literal_eval(item)

            print "[%s]  ------->   Suporte: %s " %(nameGenerator(temp), (float(LK[item])/float(len(transactions))))

            LKFINAL.append(temp)


    return LKFINAL


def generateConfidence(LK, k):


    aux = list()

    if k == 1:
        return
    else:
        for i in range (len(LK)):
            for i in range(1,k):
                aux.append(LK[i])



def nameGenerator(itemset):


        fim = ""
        for product in itemset:
            sql = cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(product))
            temp = cursor.fetchone()
            fim = fim +" "+temp[0]
        return fim



def ruleToName(rule0, rule1):



    fim0 = ""
    for item in rule0:
        sql = cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(item))
        temp = cursor.fetchone()
        fim0 = fim0 + " "+temp[0]


    fim1 = ""
    for item in rule1:
        sql = cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(item))
        temp = cursor.fetchone()
        fim1 = fim1 + " "+temp[0]

    print fim0 + "------>"+ fim1


def confidence(rule0, rule1):

    global transactions

    rule0set = map(set, [rule0])
    rule1set = map(set, [rule1])

    #resultset = rule0set.

    #for item in transactions:






def apriori():

    global transactions
    global cursor

    dbConnection()
    checkTransactions()

    LK = buildC1()

    while len(LK) > 1:



        for item in LK:
            if len(item) > 1:
                for rule in helptools.conjuntoDasPartes(item):

                    ruleToName(rule[0],rule[1])
                    confidence(rule[0], rule[1])



        LK = buildLK(LK)




apriori()
