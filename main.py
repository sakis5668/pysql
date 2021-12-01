import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Ui_main import Ui_MainWindow

from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

if __name__ == "__main__":

    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName("test.db")

    app = QApplication(sys.argv)

    if not connection.open():
        QMessageBox.critical(
            None,
            "Error !",
            "Database error: %s" % connection.lastError().databaseText(),
        )
        sys.exit(1)


    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
