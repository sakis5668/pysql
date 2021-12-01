import sys

from PyQt5.QtSql import QSqlTableModel
from ui.Ui_main import Ui_MainWindow
from models.artists import Artist

class Window(Ui_MainWindow):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.actionExit.triggered.connect(lambda: sys.exit(0))
        self.testButton.clicked.connect(self.testButtonPressed)


    def testButtonPressed(self):

        model=Artist.all()

        for i in range(0, model.rowCount()):
            first=model.record(i).value("first_name")
            last=model.record(i).value("last_name")
            print(f"{first}, {last}")