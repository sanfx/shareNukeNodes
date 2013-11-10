import datetime
from PySide import QtGui,QtCore
from PyQt4.QtCore import pyqtSlot
import sys
import os

class SendNukeNodes(QtGui.QMainWindow):
	def __init__(self):
		super(SendNukeNodes, self).__init__()
		self._lookInPath = "/usr/people/sanjeev-ku"
		self.filesList = os.listdir(self._lookInPath)
		print self.filesList
		self.watchMyNodesBin()

	def watchMyNodesBin(self):
		self.fileSysWatcher = QtCore.QFileSystemWatcher()
		self.fileSysWatcher.addPath(self._lookInPath)
		QtCore.QObject.connect(self.fileSysWatcher,QtCore.SIGNAL("directoryChanged(QString)"), self,	   
			QtCore.SLOT("slotDirChanged(QString)"))	
		# get list of files as nodes
		self.newFilesList = os.listdir(self._lookInPath)


	def _connections(self):
		pass

	def recievedNodesFromUser(self):
		newUsrNodeFile =  list(set(os.listdir(self._lookInPath))^set(self.filesList))[0]
		userRecvdFrom = newUsrNodeFile.split(".")[0]
		self.filesList.append(newUsrNodeFile)
		print newUsrNodeFile
		return userRecvdFrom

	@pyqtSlot("QString")   
	def slotDirChanged(self, userNodes):
		userName = self.recievedNodesFromUser()
		QtGui.QMessageBox.about(self, "Hello %s" % os.getenv('USER'), "Recieved Nodes from %s." % userName)

def main():
	app     = QtGui.QApplication(sys.argv)
	window    = SendNukeNodes()  
	app.exec_()

if __name__ == '__main__':
	main()
	