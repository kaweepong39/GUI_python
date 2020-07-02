import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox, QAction, QMainWindow
# from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

# defining method
class App(QWidget):

  def __init__(self):
    
    super().__init__()
    self.title = "PyQt5 simple windown"
    self.left = 150
    self.top = 150
    self.width = 500
    self.height = 450
    self.initUI()

  # Defining Method for Titel
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)

    # Create textbox
    self.textbox = QLineEdit(self)
    self.textbox.move(20, 20)
    self.textbox.resize(280, 40)

    # Create button
    self.button = QPushButton('Show text', self)
    # self.button.setToolTip("This is example button")
    self.button.move(20, 80)
    self.button.clicked.connect(self.on_click)
    self.show()

  # Actoin on clik button
  @pyqtSlot()
  def on_click(self):
    textboxValue = self.textbox.text()
    QMessageBox.question(self, "Message", "You typed: {} ".format(textboxValue), QMessageBox.Ok, QMessageBox.Cancel)
    self.textbox.setText("")
    
# main method to Run the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
