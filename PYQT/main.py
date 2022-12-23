import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

from test import First
from test1 import second

form_class = uic.loadUiType("main.ui")[0]

class WindowClass(QWidget, form_class) :
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.MoveFirst)
        self.pushButton_2.clicked.connect(self.Movesecond)

    def MoveFirst(self):
        widget.setCurrentIndex(1)

    def Movesecond(self):
        widget.setCurrentIndex(2)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    mainWindow = WindowClass()
    button1 = First()
    button2 = second()

    widget.addWidget(mainWindow)
    widget.addWidget(button1)
    widget.addWidget(button2)

    widget.setFixedHeight(275)
    widget.setFixedWidth(390)
    widget.show()

    app.exec_()