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

class Create (qt.QWidget):
    '''
    This is the Create class which will be used to create new records in the database.
    '''
    def __init__(self, parent=None):
        super(Create, self).__init__(parent)
        self.initUI()
        
    def initUI(self):
                #LABELS
        self.Fname = qt.QLabel('First name: ')
        self.Lname = qt.QLabel('Last name: ')
        self.Username = qt.QLabel('Username: ')
        self.Password = qt.QLabel('Password: ')
        self.Phone = qt.QLabel('Phone Number: ')
        self.Email = qt.QLabel('E-mail address: ')
        self.Permissions = qt.QLabel('User Permissions: ')       
        
                #TEXTFIELDS
        self.fnameEdit = qt.QLineEdit()
        self.fnameEdit.setObjectName ("fname")
        self.lnameEdit = qt.QLineEdit()
        self.lnameEdit.setObjectName ("lname")
        self.usernameEdit = qt.QLineEdit()
        self.usernameEdit.setObjectName ("username")
        self.passwordEdit = qt.QLineEdit()
        self.passwordEdit.setObjectName ("password")
        self.phoneEdit = qt.QLineEdit()
        self.phoneEdit.setObjectName ("phone")
        self.emailEdit = qt.QLineEdit()
        self.emailEdit.setObjectName ("email")
        self.permissionsEdit = qt.QLineEdit()
        self.permissionsEdit.setObjectName ("permissions")
        
                #BUTTONS
        self.submit = qt.QPushButton(self)
        self.submit.setObjectName("submit")
        self.submit.setText("Submit")
        
        self.close = qt.QPushButton(self)
        self.close.setObjectName("close")
        self.close.setText("Close") 
        
                #LAYOUT
        form = qt.QFormLayout()
        form.setSpacing(10)
                
                #ADDING THE WIDGETS TO THE LAYOUT
        form.addWidget(self.Fname)
        form.addWidget(self.fnameEdit)
        form.addWidget(self.Lname)
        form.addWidget(self.lnameEdit)
        form.addWidget(self.Username)
        form.addWidget(self.usernameEdit)
#        form.addWidget(self.Password)
#        form.addWidget(self.passwordEdit)
#        form.addWidget(self.Phone)
#        form.addWidget(self.phoneEdit)
#        form.addWidget(self.Email)
#        form.addWidget(self.emailEdit)
#        form.addWidget(self.Permissions)
#        form.addWidget(self.permissionsEdit)
        form.addWidget(self.submit)
        form.addWidget(self.close)
        
                #SETTING THE LAYOUT TO THE OBJECT
        self.setLayout(form)
        self.connect(self.submit, SIGNAL("clicked()"), self.submitQuery)
        self.connect(self.close, SIGNAL("clicked()"), self.quitApp)
        
    def submitQuery (self):
        if self.fnameEdit.text() != '' and self.lnameEdit.text() != '' and self.usernameEdit.text() != '' and self.passwordEdit.text() != '' and self.phoneEdit.text() != '' and self.emailEdit.text() != '' and self.permissionsEdit.text():
            myCursor = db.name().cursor()
            try:
#                myCursor.execute ("INSERT INTO User (User_Fname,User_Lname,User_Username,User_Password,User_Phone,User_Email,User_Permissions) VALUES (%s,%s,%s,%s,%s,%s,%s)", [self.fnameEdit.text(), self.lnameEdit.text(), self.usernameEdit.text(), self.passwordEdit.text(), self.phoneEdit.text(), self.emailEdit.text(), self.permissionsEdit.text()])
                myCursor.execute ("INSERT INTO User (User_Fname,User_Lname,User_Username) VALUES (%s,%s,%s)", [self.fnameEdit.text(), self.lnameEdit.text(), self.usernameEdit.text()])
                print "Successfully inserted"
                db.name().commit()
            except mdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                db.name().rollback()
                print "Could not successfully insert!"
                sys.exit(1)
        else:
            alertPopup = qt.QMessageBox()
            alertPopup.setText("Some fields are still empty!")
            alertPopup.setIcon(alertPopup.Critical)
            alertPopup.exec_()
            
    def quitApp (self):        
        db.name().close()
        sys.exit(0)
