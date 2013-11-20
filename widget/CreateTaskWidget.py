'''
Created on Jul 23, 2012

@author: sicp
'''

import sys
import MySQLdb as mdb
import datetime

from PyQt4 import QtGui as qt
from DBConnection import Connection
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import QDate

db = Connection()
myCursor = db.name().cursor()

class Create (qt.QWidget):
    '''
    This is the Create class which will be used to create new records in the database.
    '''
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.userLabel = qt.QLabel('For user: ')
        self.usersCombo = qt.QComboBox(self)
        try:
            myCursor.execute ("SELECT DISTINCT User_Username FROM User ORDER BY User_Username ASC")
            usersResult = myCursor.fetchall()
            for row in usersResult:
                self.usersCombo.insertItem (1, row[0])
        except mdb.Error, e:
            print "Error %d: %s" % (e.args[0], e.args[1])
            sys.exit(1) 
            
        self.dueLabel = qt.QLabel('Date due: ')
        self.subjectLabel = qt.QLabel('Subject: ')
        self.subjectEdit = qt.QTextEdit()
        self.submit = qt.QPushButton(self)
        self.submit.setText("Submit")
        self.close = qt.QPushButton(self)
        self.close.setText("Close") 
        
        self.form = qt.QFormLayout()
        self.form.setSpacing(5)
        
        self.calendar = qt.QCalendarWidget()
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        
        self.spacer = qt.QSpacerItem(100, 10, qt.QSizePolicy.Expanding, qt.QSizePolicy.Fixed)
        self.spacer2 = qt.QSpacerItem(100, 10, qt.QSizePolicy.Expanding, qt.QSizePolicy.Fixed)
        
        self.form.addWidget(self.userLabel)
        self.form.addWidget(self.usersCombo)
        self.form.addItem(self.spacer)
        self.form.addWidget(self.dueLabel)
        self.form.addWidget(self.calendar)
        self.form.addItem(self.spacer2)
        self.form.addWidget(self.subjectLabel)
        self.form.addWidget(self.subjectEdit)
        self.form.addWidget(self.submit)
        self.form.addWidget(self.close)
        
        self.setLayout(self.form)
        self.connect(self.submit, SIGNAL("clicked()"), self.submitQuery)
        self.connect(self.close, SIGNAL("clicked()"), self.quitApp)
        
    def submitQuery (self):
        userID = ""
        dateAddedValue = datetime.date.today()
        dateDueValue = self.calendar.selectedDate()
        
        if self.subjectEdit.toPlainText() != '':
            myCursor.execute ("SELECT User_ID FROM User WHERE User_Username = %s", [self.usersCombo.currentText()])
            result = myCursor.fetchall()
            for row in result:
                userID = row[0]
            try:
                print dateDueValue.toPyDate()
                myCursor.execute ("INSERT INTO Tasks (User_ID, Task_DateAdded, Task_DateDue, Task_Subject) VALUES (%s,%s,%s,%s)", [userID, dateAddedValue, dateDueValue.toPyDate(), self.subjectEdit.toPlainText()])
                alertPopup = qt.QMessageBox()
                alertPopup.setText("Successfully inserted!")
                alertPopup.setIcon(alertPopup.Information)
                alertPopup.exec_()
                db.name().commit()
                self.subjectEdit.setPlainText("")
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                db.name().rollback()
                alertPopup = qt.QMessageBox()
                alertPopup.setText("Could not successfully insert!")
                alertPopup.setIcon(alertPopup.Critical)
                alertPopup.exec_()
                sys.exit(1)
        else:
            alertPopup = qt.QMessageBox()
            alertPopup.setText("Some fields are still empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
            
    def quitApp (self):        
        db.name().close()
        sys.exit(0) 
