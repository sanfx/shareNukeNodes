import datetime
from PySide import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot
import sys
import os

class WatchNukeNodesBin(QtGui.QMainWindow):
	def __init__(self):
		super(WatchNukeNodesBin, self).__init__()
		self._lookInPath = "/usr/people/sanjeev-ku"
		self.fileSysWatcher = QtCore.QFileSystemWatcher()
		self.filesList = os.listdir(self._lookInPath)
		print self.filesList
		self.watchMyNodesBin()

	def watchMyNodesBin(self):
		self.fileSysWatcher.addPath(self._lookInPath)
		QtCore.QObject.connect(self.fileSysWatcher,QtCore.SIGNAL("directoryChanged(QString)"), self,	   
			QtCore.SLOT("slotDirChanged(QString)"))	
		# get list of files as nodes
		self.newFilesList = os.listdir(self._lookInPath)


	def _connections(self):
		pass

	def recievedNodesFromUser(self):
		newUsrNodeFile = list(set(os.listdir(self._lookInPath)).symmetric_difference(self.filesList))[0]
		if not newUsrNodeFile in self.filesList:
			userRecvdFrom = newUsrNodeFile.split(".")[0]
			self.filesList.append(newUsrNodeFile)
			return userRecvdFrom
		return

	@pyqtSlot("QString")   
	def slotDirChanged(self, userNodes):
		userName = self.recievedNodesFromUser()
		if userName:
			QtGui.QMessageBox.about(self, "Hello %s" % os.getenv('USER'), "Recieved Nodes from %s." % userName)

def main():
	app     = QtGui.QApplication(sys.argv)
	window    = WatchNukeNodesBin()  
	app.exec_()

if __name__ == '__main__':
	main()
	