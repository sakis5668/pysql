import sys
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from window import Window


def main():
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
    window = Window(MainWindow)
    MainWindow.show()
    app.exec_()


if __name__ == "__main__":
    main()
