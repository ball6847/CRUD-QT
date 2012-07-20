'''
Created on Jul 18, 2012

@author: sicp
'''

import sys
import CreateWidget
import RetrieveWidget
from PyQt4 import QtGui as qt

def main():
    '''
    This is the GUI module where all of the program's elements come together in a pretty little tabbed window.
    '''
    app = qt.QApplication(sys.argv)

    CreateTab = CreateWidget.Create()
    RetrieveTab = RetrieveWidget.Retrieve()
    
    tabs = qt.QTabWidget()
    tabs.addTab (CreateTab, "Create User")
    tabs.addTab (RetrieveTab, "Search")
    
    tabs.setGeometry(300, 300, 300, 300)
    tabs.setWindowTitle('CRUD')
    tabs.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
