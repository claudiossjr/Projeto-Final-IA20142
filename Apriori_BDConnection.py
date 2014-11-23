from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb

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

    transactions = [[] for i in range(numberOfTransactions+1)]

    cursor.execute("SELECT * FROM Compra")
    auxtransactions = cursor.fetchall()

    for tuple in auxtransactions:
       transactions[int(tuple[1])].append(int(tuple[0]))

    # print de cada transacao
    for item in transactions:
        print item

def buildC1():

    global transactions




    transactions = map(set, transactions)



    C1 = {}

    for ID in transactions:
        for product in ID:
            if not C1.has_key(product): C1[product] = 1
            else: C1[product] += 1


    # print do C1. {idProduto, Quantidade}
    for item in C1:
        print " Item: %s Quantidade %s " % (item ,C1[item])

    LAUX = {}

    for item in C1:
        if (float(C1[item]) / float(len(transactions))) > suport:
            LAUX[item] = C1[item]
            cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" % (item) )
            productName = cursor.fetchall()

            for aux in productName:
                print "%s -----> Suporte: %s " % (aux[0], float(C1[item]) / float(len(transactions)))


    L1 = [0 for i in range(len(LAUX))]


    i = 0
    for item in LAUX:
        L1[i] = item
        i = i+1



    return L1,LAUX



    #joinOperation(L1,transactions)


def apriori():

    global transactions

    dbConnection()
    checkTransactions()
    L1,LAUX =buildC1()

    LN = []

    for item in L1:
        LN.append(set([item]))


    K = 0
    Ck = newJoinOperation(LN,K)
    buildCk(Ck)




def buildCk(Ck):

    lk = []
    ckn = [0 for i in range(len(Ck))]

    global transactions




    for i in range(len(Ck)):
        for j in range(len(transactions)):
                if Ck[i].issubset(transactions[j]):
                    ckn[i] += 1

    for item in ckn:
        print item






def newJoinOperation(L,k):

    Ck = []


    for i in range(len(L)-1):
        for j in range(i+1, len(L)):
            listaux = list(L[i].union(L[j]))
            Ck.append(listaux)

    Ck = map(set, Ck)

    return Ck


def joinOperation(LK,transactions):

    LK = {}

    auxList = L1.keys()
    newListofTuples = list();

    for i in range(0, len(auxList)):
        for j in range(i+1, len(auxList)):
            newListofTuples.append([auxList[i],auxList[j]])

    for item in newListofTuples:
        print item

    print "___________________"
    print newListofTuples [0][0]
    print newListofTuples [0][1]
    print newListofTuples [1][0]
    print newListofTuples [1][1]
    print newListofTuples [2][0]
    print newListofTuples [2][1]

    saveRules(len(newListofTuples[0]))

def saveRules(K):

    sql = "CREATE TABLE L%s (id INT, element INT)" %(K)

    print sql


def checkSubset(transactions, tupleList):

    CK = {}
    i = 0
    for ID in transactions:
        for item in ID:
            print ""
    print tupleList[0][0]


apriori()
