'''
Created on Jul 18, 2012

@author: sicp
'''

import MySQLdb
import sys

class Connection ():
    '''
    This is the Connection class where the database connection is established, all other classes will include this class to be able to connect to the database.
    '''
    def __init__(self):
        try:
           self.conn = MySQLdb.connect(host="localhost", user="root",
                                 passwd="ONGOINGwarfare1+2+3+", db="CRUDQT")
        except MySQLdb.Error, e:
           print "Error %d: %s" % (e.args[0], e.args[1])
           sys.exit(1)
                   
    def TearDown(self):
        self.conn.close()
            
    def name(self):
        return self.conn
