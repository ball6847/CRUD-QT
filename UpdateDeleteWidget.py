'''
Created on Jul 20, 2012

@author: sicp
'''

import sys
import MySQLdb as mdb

from PyQt4 import QtGui as qt
from DBConnection import Connection
from PyQt4.QtCore import SIGNAL
import PyQt4
db = Connection()
myCursor = db.name().cursor()

class UpdateDelete (qt.QWidget):
    '''
    This class is used to demonstrate the Modify/Delete functionality over the tables 'Task' and 'User'
    '''
    
    def __init__(self, parent=None):
        super(UpdateDelete, self).__init__(parent)
        self.initUI()
        
    def initUI (self):
        self.topLabel = qt.QLabel ("Below are your users/tasks")
        self.resultsTable = qt.QTableWidget ()
        self.populateButton = qt.QPushButton('Populate')
        self.populateButton.clicked.connect(self.populate)
        
        self.grid = qt.QGridLayout()
        self.grid.setSpacing(5)
        
        self.grid.addWidget (self.resultsTable)
        self.grid.addWidget (self.populateButton)
        
        self.setLayout(self.grid)
        
    def populate (self):
        try:
            myCursor.execute ("SELECT COUNT(User_Username) FROM User")
            result = myCursor.fetchall()
            for row in result:
                numberOfUsers = row[0]
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
            
        nrows, ncols = numberOfUsers, 5
        self.resultsTable.setSortingEnabled(False)
        self.resultsTable.setRowCount(nrows)
        self.resultsTable.setColumnCount(ncols)
        
        headerDict = ["First name", "Last name", "Username", "Password", "E-mail"]
        for index in range(len(headerDict)):    
            self.resultsTable.setHorizontalHeaderItem(index, qt.QTableWidgetItem(headerDict[index]))
        
        try:
            myCursor.execute ("SELECT * FROM User")
            result = myCursor.fetchall()
            for i in range (nrows):
                for j in range (ncols):
                    item = qt.QTableWidgetItem('%s' % (result[i][j + 1]))
                    item.setFlags(PyQt4.QtCore.Qt.ItemIsEnabled)
                    self.resultsTable.setItem(i, j, item)
            
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1)
        
        self.resultsTable.setSortingEnabled (True)
        
