__author__ = 'joaolucas'


import MySQLdb


def connectBD():


    print "Insert hostname"
    host = raw_input()
    print "Insert Username"
    username = raw_input()
    print "Insert your password"
    password = raw_input()
    print "Insert Database"
    database = raw_input()

    db = MySQLdb.connect(host,username,password,database)
    cursor = db.cursor()