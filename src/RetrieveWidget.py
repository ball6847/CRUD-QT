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
        self.searchByFirstnameEdit = qt.QLineEdit()
        self.searchByUsernameEdit = qt.QLineEdit()
        self.resultLabel = qt.QLabel()
        self.fromTableLabel = qt.QLabel()
        self.fromTableLabel.setText("From table:")

        self.searchByFirstnameButton = qt.QPushButton(self)
        self.searchByFirstnameButton.setText("by First Name")
        self.searchByUsernameButton = qt.QPushButton(self)
        self.searchByUsernameButton.setText("by Username")
        
        self.close = qt.QPushButton(self)
        self.close.setText("Close")
        
        self.tablesCombo = qt.QComboBox(self)
        try:
            myCursor.execute ("SHOW TABLES")
            tablesResult = myCursor.fetchall()
            for row in tablesResult:
                self.tablesCombo.insertItem (1, row[0])
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1) 

        grid = qt.QGridLayout()
        grid.setSpacing(10)
                
        grid.addWidget(self.searchByFirstnameEdit, 1, 0)
        grid.addWidget(self.searchByFirstnameButton, 1, 1)
        grid.addWidget(self.fromTableLabel, 2, 0,)
        grid.addWidget(self.tablesCombo, 2, 1)
        grid.addWidget(self.searchByUsernameEdit, 3, 0)
        grid.addWidget(self.searchByUsernameButton, 3, 1)
        grid.addWidget(self.resultLabel, 4, 0, 1, 2)
        grid.addWidget(self.close, 5, 0, 1, 2)
        
        self.setLayout(grid)
        self.connect(self.searchByFirstnameButton, SIGNAL("clicked()"), self.byFirstnameQuery)
        self.connect(self.searchByUsernameButton, SIGNAL("clicked()"), self.byUsernameQuery)
        self.connect(self.close, SIGNAL("clicked()"), self.quitApp)
        
    def byFirstnameQuery (self):
        if self.searchByFirstnameEdit.text() != '' and self.tablesCombo.currentText() == 'User':
            try:
                myCursor.execute ("SELECT User_Username FROM User WHERE User_Fname = %s", [self.searchByFirstnameEdit.text()])
                searchResult = myCursor.fetchall()
                if searchResult == None:
                    alertPopup = qt.QMessageBox()
                    alertPopup.setText("Nothing about " + self.searchByFirstnameEdit.text() + " was found in this table")
                    alertPopup.setIcon(alertPopup.Critical)
                    alertPopup.exec_()
                else:
                    for row in searchResult:
                            self.resultLabel.setText(self.searchByFirstnameEdit.text() + " has the username: " + row[0])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        elif self.searchByFirstnameEdit.text() != '' and self.tablesCombo.currentText() == 'Tasks':
            try:
                myCursor.execute ("SELECT Task_Subject FROM Tasks WHERE User_ID = (SELECT User_ID FROM User WHERE User_Fname = %s)", self.searchByFirstnameEdit.text())
                searchResult = myCursor.fetchall()
                for row in searchResult:
                    if row[0] == '': self.resultLabel.setText("Nothing about " + self.searchByFirstnameEdit.text() + " was found in this table")
                    else: self.resultLabel.setText(self.searchByFirstnameEdit.text() + " has to: " + row[0])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        else:
            alertPopup = qt.QMessageBox()
            alertPopup.setWindowTitle ("Warning!")
            alertPopup.setText("Search field is empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
            
    def byUsernameQuery (self):
        if self.searchByUsernameEdit.text() != '' and self.tablesCombo.currentText() == 'User':
            try:
                myCursor.execute ("SELECT User_Fname FROM User WHERE User_Username = %s", [self.searchByUsernameEdit.text()])
                searchResult = myCursor.fetchall()
                if searchResult == -1:
                    alertPopup = qt.QMessageBox()
                    alertPopup.setText("Nothing about " + self.searchByUsernameEdit.text() + " was found in this table")
                    alertPopup.setIcon(alertPopup.Critical)
                    alertPopup.exec_()
                else:
                    for row in searchResult:
                            self.resultLabel.setText(self.searchByUsernameEdit.text() + " has the username: " + row[0])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        elif self.searchByUsernameEdit.text() != '' and self.tablesCombo.currentText() == 'Tasks':
            try:
                myCursor.execute ("SELECT Task_Subject FROM Tasks WHERE User_ID = (SELECT User_ID FROM User WHERE User_Username = %s)", self.searchByUsernameEdit.text())
                searchResult = myCursor.fetchall()
                for row in searchResult:
                    if row[0] == '': self.resultLabel.setText("Nothing about " + self.searchByUsernameEdit.text() + " was found in this table")
                    else: self.resultLabel.setText(self.searchByUsernameEdit.text() + " has to: " + row[0])
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                sys.exit(1)
        else:
            alertPopup = qt.QMessageBox()
            alertPopup.setWindowTitle ("Warning!")
            alertPopup.setText("Search field is empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
            
    def quitApp (self):
        db.name().close()
        sys.exit(0)
