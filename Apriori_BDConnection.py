__author__ = 'joaolucas'


import MySQLdb




print "Insert hostname"
host = "localhost"#raw_input()
print "Insert Username"
username = "joao" #raw_input()
print "Insert your password"
password = "1234" #raw_input()
print "Insert Database"
database = "sakila" #raw_input()

db = MySQLdb.connect(host,username,password,database)
cursor = db.cursor()


def checkNumberOfRows():

    cursor.execute("SELECT COUNT(*) FROM rental")
    numberOfRows = cursor.fetchone()
    print numberOfRows


checkNumberOfRows()
