import datetime
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 
import sys

class MyMainWindow(QMainWindow):
  def __init__(self):
    QMainWindow.__init__(self)
    self.label = QLabel("No Change Detected..")
    self.setCentralWidget(self.label)
    self.setWindowTitle("Detect Dir Change")
   
  @pyqtSlot("QString")   
  def slotDirChanged(self,fileName):
    now = datetime.datetime.now()
    self.label.setText("Detected Directory Change at %s:%s:%s" % (now.hour,now.minute,now.second))

def main():
	app 		= QApplication(sys.argv)
	fileSysWatcher	= QFileSystemWatcher()	
	window 		= MyMainWindow()			

	fileSysWatcher.addPath("/Users/sanjeevkumar/Desktop")	
	window.show()  

	QObject.connect(fileSysWatcher,SIGNAL("directoryChanged(QString)"),
			window,	   SLOT("slotDirChanged(QString)"))	  
	return app.exec_()

if __name__ == '__main__':
  main()
	