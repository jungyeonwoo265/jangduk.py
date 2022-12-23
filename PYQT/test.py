import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_widget = uic.loadUiType("test.ui")[0]

class First(QWidget, form_widget) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.MoveParent)

    def MoveParent(self):
        self.parent().setCurrentIndex(0)

# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     myWindow = First()
#     myWindow.show()
#     app.exec_()