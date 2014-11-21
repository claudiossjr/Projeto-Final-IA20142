from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb

numberOfRows = 0
suport = 0.4

def dbConnection():
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
    checkTransactions(cursor)


def checkTransactions(cursor):

    cursor.execute("SELECT COUNT(DISTINCT idCliente) FROM Compra")
    numberOfTransactions = int(cursor.fetchone()[0])

    transactions = [[] for i in range(numberOfTransactions+1)]

    cursor.execute("SELECT * FROM Compra")
    auxtransactions = cursor.fetchall()

    for tuple in auxtransactions:
       transactions[int(tuple[1])].append(int(tuple[0]))

    buildC1(transactions, cursor)

def buildC1(transactions, cursor):

    C1 = {}

    for ID in transactions:
        for product in ID:
            if not C1.has_key(product): C1[product] = 1
            else: C1[product] += 1

    L1 = {}

    for item in C1:
        if (float(C1[item]) / float(len(transactions))) > suport:
            L1[item] = C1[item]
            cursor.execute("SELECT nome FROM Produtos WHERE idProdutos = %s" % (item) )
            productName = cursor.fetchall()

            for aux in productName:
                print "%s -----> Suporte: %s " % (aux[0], float(C1[item]) / float(len(transactions)))


dbConnection()
