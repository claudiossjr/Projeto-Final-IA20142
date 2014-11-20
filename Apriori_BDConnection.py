from PIL.ImImagePlugin import number

__author__ = 'joaolucas'


import MySQLdb




print "Insert hostname"
host = "localhost"#raw_input()
print "Insert Username"
username = "root" #raw_input()
print "Insert your password"
password = "423123" #raw_input()
print "Insert Database"
database = "sakila" #raw_input()

db = MySQLdb.connect(host,username,password,database)
cursor = db.cursor()

numberOfRows = 0

def checkNumberOfRows():

    cursor.execute("SELECT COUNT(*) FROM rental")
    numberOfRows = cursor.fetchone()
    numberOfRows = numberOfRows[0]
    print numberOfRows


checkNumberOfRows()
