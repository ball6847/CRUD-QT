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

class Create (qt.QWidget):
    '''
    This is the Create class which will be used to create new records in the database.
    '''
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
        self.fnameLabel = qt.QLabel('First name: ')
        self.lnameLabel = qt.QLabel('Last name: ')
        self.usernameLabel = qt.QLabel('Username: ')
        self.passwordLabel = qt.QLabel('Password: ')
        self.emailLabel = qt.QLabel('E-mail address: ')
        
        self.fnameEdit = qt.QLineEdit()
        self.lnameEdit = qt.QLineEdit()
        self.usernameEdit = qt.QLineEdit()
        self.passwordEdit = qt.QLineEdit()
        self.emailEdit = qt.QLineEdit()
        
        self.submit = qt.QPushButton(self)
        self.submit.setText("Submit")
        
        self.close = qt.QPushButton(self)
        self.close.setText("Close")
        
        self.spacer = qt.QSpacerItem(100, 100, qt.QSizePolicy.Expanding, qt.QSizePolicy.Fixed)
        
        self.form = qt.QFormLayout()
        self.form.setSpacing(5)
        
        self.form.addWidget(self.fnameLabel)
        self.form.addWidget(self.fnameEdit)
        self.form.addWidget(self.lnameLabel)
        self.form.addWidget(self.lnameEdit)
        self.form.addWidget(self.usernameLabel)
        self.form.addWidget(self.usernameEdit)
        self.form.addWidget(self.passwordLabel)
        self.form.addWidget(self.passwordEdit)
        self.form.addWidget(self.emailLabel)
        self.form.addWidget(self.emailEdit)
        self.form.addItem(self.spacer)
        self.form.addWidget(self.submit)
        self.form.addWidget(self.close)
        
        self.setLayout(self.form)

        self.connect(self.submit, SIGNAL("clicked()"), self.submitQuery)
        self.connect(self.close, SIGNAL("clicked()"), self.quitApp)
        
    def submitQuery (self):
        if self.fnameEdit.text() != '' and self.lnameEdit.text() != '' and self.usernameEdit.text() != '':
#        and self.passwordEdit.text() != '' and self.phoneEdit.text() != '' and self.emailEdit.text() != '' and self.permissionsEdit.text():
            try:
                myCursor.execute ("INSERT INTO User (User_Fname,User_Lname,User_Username,User_Password,User_Email) VALUES (%s,%s,%s,%s,%s)", [self.fnameEdit.text(), self.lnameEdit.text(), self.usernameEdit.text(), self.passwordEdit.text(), self.emailEdit.text()])
                alertPopup = qt.QMessageBox()
                alertPopup.setText("Successfully inserted!")
                alertPopup.setIcon(alertPopup.Information)
                alertPopup.exec_()
                db.name().commit()
                self.fnameEdit.setText("")
                self.lnameEdit.setText("")
                self.usernameEdit.setText("")
                self.passwordEdit.setText("")
                self.emailEdit.setText("")
                self.fnameEdit.setFocus()
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
