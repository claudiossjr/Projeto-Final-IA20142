from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb
import ast
from JoinFile1 import Util,HelpTools

util = Util()

helptools = HelpTools()

numberOfTransactions = 0
suport = 0.01
transactions = -1
cursor = -1

def dbConnection():

    #connect to DB

    global cursor

    #print "Insert hostname"
    host = "localhost"#raw_input()
    #print "Insert Username"
    username = "root" #raw_input()
    #print "Insert your password"
    password = "423123" #raw_input()
    #print "Insert Database"
    database = "teste" #raw_input()

    db = MySQLdb.connect(host, username, password, database)
    cursor = db.cursor()

'''
def transanctionsFromSakila():

    global cursor

    cursor.execute("Select rental.rental_id, inventory.inventory_id ,film.title from film inner join inventory on film.film_id = inventory.film_id inner join rental on rental.inventory_id = inventory.inventory_id")


    transacoes = cursor.fetchall()
    globalList = list()
    for transacao in transacoes:
        temp = list()
        print transacao
        temp.append(transacao[0])
        temp.append(transacao[1])
        temp.append(transacao[2])
        globalList.append(temp)
    print globalList

'''



def checkTransactions():

    #check transactions made for each client

    global cursor
    global transactions

    cursor.execute("SELECT COUNT(DISTINCT idCliente) FROM Compra")
    numberOfTransactions = int(cursor.fetchone()[0])
    #print numberOfTransactions

    transactions = [[] for i in range(1010)]

    cursor.execute("SELECT * FROM Compra")
    auxtransactions = cursor.fetchall()

    for tuple in auxtransactions:
        transactions[int(tuple[1])].append(int(tuple[0]))


    '''# print de cada transacao
    print "TRANSACTIONS"
    for item in transactions:
        transactionsToName(item)
    '''

    transactions = map(set, transactions)

def transactionsToName(transaction):

    global cursor
    transacationname = ""
    for item in transaction:
        cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(item))
        temp = cursor.fetchone()
        transacationname = transacationname +  temp[0]+"    "
    print "[" + transacationname + "]"

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
        print itemset
        print itemset
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



def ruleToName(rule):
    listTemp = list()

    for item in rule:
        sql = cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" %(item))
        aux = cursor.fetchone()
        #print aux[0]
        temp = aux[0]
        #print temp
        listTemp.append(temp)
    #print listTemp
    return listTemp



def suportCalculator(baselist):




    baseset = map(set, [baselist])


    numberOfOccurrences = 0.0
    for transaction in transactions:
        if baseset[0].issubset(transaction):
            numberOfOccurrences += 1

    return numberOfOccurrences/float(len(transaction))






def confidence(rule0, rule1):


    unionset = helptools.unionSet(rule0,rule1)

    uniosetsuport = suportCalculator(unionset)

    rule0suport = suportCalculator(rule0)

    print rule0," -> ",rule1,"  ",uniosetsuport/rule0suport

    return uniosetsuport/rule0suport





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
                    confianca = confidence(rule[0], rule[1])

                    if confianca > 0:
                        print nameGenerator(rule[0])," -> ",nameGenerator(rule[1]), " --  confianca -> ",confianca
        LK = buildLK(LK)



apriori()
#dbConnection()
#transanctionsFromSakila()