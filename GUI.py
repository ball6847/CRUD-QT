'''
Created on Jul 18, 2012

@author: sicp
'''

import sys
from PyQt4 import QtGui as qt

from widget import CreateUserWidget, CreateTaskWidget, RetrieveWidget, UpdateDeleteWidget


def main():
    '''
    This is the GUI module where all of the program's elements come together in a pretty little tabbed window.
    '''
    app = qt.QApplication(sys.argv)

    CreateUserTab = CreateUserWidget.Create()
    CreateTaskTab = CreateTaskWidget.Create()
    RetrieveTab = RetrieveWidget.Retrieve()
    UpdateDeleteTab = UpdateDeleteWidget.UpdateDelete()
    
    tabs = qt.QTabWidget()
    
    tabs.addTab (CreateUserTab, "Create User")
    tabs.addTab (CreateTaskTab, "Create Task")
    tabs.addTab (RetrieveTab, "Search")
    tabs.addTab (UpdateDeleteTab, "Update/Delete")
    
    tabs.setGeometry(450, 100, 400, 520)
    tabs.setWindowTitle('CRUD')
    tabs.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
