'''
Created on Jul 20, 2012

@author: sicp
'''

import sys
import MySQLdb as mdb

from PyQt4 import QtGui as qt
from DBConnection import Connection
from PyQt4.QtCore import SIGNAL

db = Connection()
myCursor = db.name().cursor()

class Retrieve (qt.QWidget):
    '''
    This is the Retrieve class which will be used to retrieve records from the database and display them to the user.
    '''
    def __init__(self, parent=None):
        super(Retrieve, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.searchEdit = qt.QLineEdit()
        self.searchEdit.setObjectName ("search")
        
        self.resultLabel = qt.QLabel()
        self.resultLabel.setObjectName ("fromTableLabel")
        self.fromTableLabel = qt.QLabel()
        self.fromTableLabel.setObjectName ("fromTableLabel")
        self.fromTableLabel.setText("From table:")

                #BUTTONS
        self.searchButton = qt.QPushButton(self)
        self.searchButton.setObjectName("search")
        self.searchButton.setText("Search")
        
        self.close = qt.QPushButton(self)
        self.close.setObjectName("close")
        self.close.setText("Close")
        
                #COMBO BOX
        self.tablesCombo = qt.QComboBox(self)
        self.tablesCombo.setObjectName ("tablesCombo")
        try:
            myCursor.execute ("SHOW TABLES")
            tablesResult = myCursor.fetchall()
            for row in tablesResult:
                self.tablesCombo.insertItem (1, row[0])
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1) 
        
                #LAYOUT
        grid = qt.QGridLayout()
        grid.setSpacing(10)
                
                #ADDING THE WIDGETS TO THE LAYOUT
        grid.addWidget(self.searchEdit, 1, 0)
        grid.addWidget(self.searchButton, 1, 1)
        grid.addWidget(self.fromTableLabel, 2, 0,)
        grid.addWidget(self.tablesCombo, 2, 1)
        grid.addWidget(self.resultLabel, 4, 0, 1, 2)
        grid.addWidget(self.close, 5, 0, 1, 2)
        
                #SETTING THE LAYOUT TO THE OBJECT
        self.setLayout(grid)
        self.connect(self.searchButton, SIGNAL("clicked()"), self.submitQuery)
        self.connect(self.close, SIGNAL("clicked()"), self.quitApp)
        
    def submitQuery (self):
        if self.searchEdit.text() != '' and self.tablesCombo.currentText() == 'User':
            try:
                myCursor.execute ("SELECT * FROM User WHERE User_Fname = %s", [self.searchEdit.text()])
                searchResult = myCursor.fetchall()
                for row in searchResult:
                        self.resultLabel.setText(self.searchEdit.text() + " has the username: " + row[3])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        elif self.searchEdit.text() != '' and self.tablesCombo.currentText() == 'Tasks':
            try:
                myCursor.execute ("SELECT * FROM Tasks WHERE User_ID = (SELECT User_ID FROM User WHERE User_Fname = %s)", self.searchEdit.text())
                searchResult = myCursor.fetchall()
                for row in searchResult:
                        self.resultLabel.setText(self.searchEdit.text() + " has to: " + row[5])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        else:
            alertPopup = qt.QMessageBox()
            alertPopup.setText("Search field is empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
            
    def quitApp (self):
        db.name().close()
        sys.exit(0)
