import sys
from PyQt4 import QtGui as qt
from widget import SiteDataTable

def main():
    app = qt.QApplication(sys.argv)

    SiteDataTableTab = SiteDataTable.Create()
    
    tabs = qt.QTabWidget()
    tabs.addTab(SiteDataTableTab, "Sites")
    tabs.setGeometry(450, 100, 400, 520)
    tabs.setWindowTitle('Site Manager')
    tabs.show()
    
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
