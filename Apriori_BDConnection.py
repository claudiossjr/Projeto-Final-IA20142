from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb




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


numberOfRows = 0

def checkNumberOfRows():

    cursor.execute("SELECT COUNT(*) FROM Compra")
    numberOfRows = cursor.fetchone()

    numberOfRowsToInt = int(numberOfRows[0])

    qtdList=[0 for i in range(numberOfRowsToInt+1)]

    cursor.execute("SELECT * FROM Compra")
    results = cursor.fetchall()

    for row in results:
        idproduto = row[0]
        idcliente = row[1]

        qtdList[idproduto] = qtdList[idproduto] + 1



    for index in range(len(qtdList)):
        print ("i %s quantidade %s " % (index, qtdList[index]))



checkNumberOfRows()