import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_widget = uic.loadUiType("test1.ui")[0]

class second(QWidget, form_widget) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.pre)

    def next(self):
        self.stackedWidget.setCurrentIndex(1)

    def pre(self):
        self.stackedWidget.setCurrentIndex(0)



# if __name__ == "__main__" :
#     app = QApplication(sys.argv)
#     myWindow = second()
#     myWindow.show()
#     app.exec_()