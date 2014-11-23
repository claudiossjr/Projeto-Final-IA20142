from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb
from JoinFile1 import Util
util = Util()

numberOfTransactions = 0
suport = 0.4
transactions = -1
cursor = -1

def dbConnection():

    #connect to DB

    global cursor

    print "Insert hostname"
    host = "localhost"#raw_input()
    print "Insert Username"
    username = "joao" #raw_input()
    print "Insert your password"
    password = "1234" #raw_input()
    print "Insert Database"
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


    # print do C1. {idProduto, Quantidade}
    for item in C1:
        print " Item: %s Quantidade %s " % (item ,C1[item])

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

    global transactions

    CK = util.makeJoins(LK)

    CK = map(set, CK)

    LK = []

    LKSUPORT = []


    for itemset in CK:
        for transaction in transactions:
            if itemset.issubset(transaction):



def apriori():

    global transactions

    dbConnection()
    checkTransactions()

    LK = buildC1()

    buildLK(LK)


apriori()
