import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QIcon
import csv

user_id = 'qkqh'

form_Class = uic.loadUiType("rental.ui")[0]

class Rental(QWidget, form_Class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('대여 및 반납')
        self.setWindowIcon(QIcon('book.jpg'))

        self.bt_gohome.clicked.connect(self.movemain)
        self.bt_Search.clicked.connect(self.Search)

        self.bt_rental.clicked.connect(self.rental)
        self.bt_return.clicked.connect(self.Return)
        self.tableWidget.clicked.connect(self.showtext)
        self.label.setText('대여 가능 여부')
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)


    def showtext(self):
        print('텍스트')
    def movemain(self):
        print('홈으로')
    def Search(self):
        book_list = list()
        self.tableWidget.clearContents()
        idx = self.book_item.currentText()
        Str = self.lineEdit.text()
        if idx == '도서명':
            idx = 4
        elif idx == '저자':
            idx = 5
        with open('광주광역시 광산구_도서목록(신가도서관)_20220818.csv', 'r') as f :
            Csv = csv.reader(f)
            for i in Csv:
                if Str in i[idx]:
                    book_list.append(i)
        self.tableWidget.setRowCount(len(book_list))
        self.tableWidget.setColumnCount(len(book_list[0]))
        for i in range(len(book_list)):
            for j in range(len(book_list[i])):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(book_list[i][j])))

    def rental(self): # 대여
        print('대여')
    def Return(self): # 반납
        print('반납')

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = Rental()
    myWindow.show()
    app.exec_()

