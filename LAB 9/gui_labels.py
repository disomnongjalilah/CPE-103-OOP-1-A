import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt Line Edit'
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y, self.width, self.height)
        self.setWindowIcon(QIcon('file_type_python_icon_130221'))

        self.textboxlbl = QLabel('Hello World', self)
        self.textboxlbl.move(100, 100)
        self.textboxlbl = QLabel('This program is written in PyCharm', self)
        self.textboxlbl.move(50, 120)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())