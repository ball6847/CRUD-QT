import sys
from PyQt4.QtGui import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QGridLayout
from PyQt4.QtCore import SIGNAL
from PyQt4.QtCore import Qt



class Create(QWidget):
	
	def __init__(self, parent=None):
		super(Create, self).__init__(parent)
		
		self.resultsTable = QTableWidget()
		self.resultsTable.setSortingEnabled(True)
		self.resultsTable.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.resultsTable.setColumnCount(3)
		self.resultsTable.setRowCount(5)
		self.resultsTable.setHorizontalHeaderItem(0, QTableWidgetItem('Domain'))
		self.resultsTable.setHorizontalHeaderItem(1, QTableWidgetItem('Created'))
		self.resultsTable.setHorizontalHeaderItem(2, QTableWidgetItem(''))
		
		for row, site in enumerate(self.get_sites()):
			self.resultsTable.setItem(row, 0, QTableWidgetItem(site['domain']))
			
			createdColumn = QTableWidgetItem(site['created'])
			createdColumn.setFlags(Qt.ItemIsEnabled)
			self.resultsTable.setItem(row, 1, createdColumn)
			
			deleteButton = QTableWidgetItem('delete')
			deleteButton.setFlags(Qt.ItemIsEnabled);
			self.resultsTable.setItem(row, 2, deleteButton)
		
		self.resultsTable.cellChanged.connect(self.handleUpdate)
		
		self.grid = QGridLayout()
		self.grid.setSpacing(5)
		self.grid.addWidget (self.resultsTable)
		self.setLayout(self.grid)
	
	def get_sites(self):
		sites = [
			{
				'id': 1,
				'domain': 'www.google.com',
				'created': '2013-11-20 12:00:08',
			},{
				'id': 2,
				'domain': 'www.yahoo.com',
				'created': '2013-11-20 12:00:09',
			},{
				'id': 3,
				'domain': 'www.msn.com',
				'created': '2013-11-20 12:00:10',
			},{
				'id': 4,
				'domain': 'www.ubuntu.com',
				'created': '2013-11-20 12:00:11',
			},{
				'id': 5,
				'domain': 'www.bing.com',
				'created': '2013-11-20 12:00:12',
			},
		]
		return sites

	def handleUpdate(self, row, column):
		print self.resultsTable.item(row, column).text()
