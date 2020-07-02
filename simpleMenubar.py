import sys
from PyQt5.QtWidgets import QApplication, QAction, QMenu, QMainWindow
# from PyQt5.QtGui import QIcon
# from PyQt5.QtCore import pyqtSlot

# defining method
class App(QMainWindow):

  def __init__(self):
    
    super().__init__()
    self.title = "PyQt5 simple menu"
    self.left = 150
    self.top = 150
    self.width = 500
    self.height = 450
    self.initUI()

  # Defining Method for Titel
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
    
    # Create menus bar
    mainMenu = self.menuBar()
    filemenu = mainMenu.addMenu("File")
    editmenu = mainMenu.addMenu("Edit")
    viewmenu = mainMenu.addMenu("View")
    searchmenu = mainMenu.addMenu("Search")
    tootmenu = mainMenu.addMenu("Tool")
    helpmenu = mainMenu.addMenu("Help")

    exitButton = QAction('Exit', self)
    exitButton.setShortcut("Ctrl+Q")
    exitButton.triggered.connect(self.close)
    filemenu.addAction(exitButton)

    # Status bar
    statusBar = QAction("Status Bar", self, checkable= True)
    statusBar.setChecked(True)
    viewmenu.addAction(statusBar)

    # Set sub menu
    zoombuttom = QMenu("Zoom", self)
    zoomIn = QAction("Zoom In", self)
    zoomIn.setShortcut("Ctrl+Plus")
    zoombuttom.addAction(zoomIn)

    zoonOut = QAction("Zoom Out", self)
    zoonOut.setShortcut("Ctrl+Minus")
    zoombuttom.addAction(zoonOut)
    viewmenu.addMenu(zoombuttom)
    self.show()

# main method to Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
