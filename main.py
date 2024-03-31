import sqlite3
import sys
import traceback

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QDialog


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("main.ui", self)
        self.table()

    def table(self) -> None:
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        cur.execute(f"""SELECT * FROM coffee""")
        db = cur.fetchall()
        self.tableWidget.setColumnCount(len(db[0]) - 1)
        self.tableWidget.setRowCount(len(db))
        self.tableWidget.setHorizontalHeaderLabels(["Name", "Roasting", "Type", "Taste", "Price", "Size"])
        for i, elemi in enumerate(db):
            for j, elemj in enumerate(elemi[1:]):
                self.tableWidget.setItem(i, j, QTableWidgetItem(elemj))
        con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
