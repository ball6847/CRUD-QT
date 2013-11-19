'''
Created on Jul 18, 2012

@author: sicp
'''

import MySQLdb
import sys
from settings import connection

class Connection ():
    '''
    This is the Connection class where the database connection is established, all other classes will include this class to be able to connect to the database.
    '''
    def __init__(self):
        try:
            self.conn = MySQLdb.connect(host=connection['host'], user=connection['user'],
                                 passwd=connection['password'], db=connection['database'])
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
                   
    def TearDown(self):
        self.conn.close()
            
    def name(self):
        return self.conn
