import sys

from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QDataWidgetMapper
from PyQt5.QtCore import Qt
from ui.Ui_main import Ui_MainWindow
from models.artists import Artist

class Window(Ui_MainWindow):

    def __init__(self, MainWindow):
        self.setupUi(MainWindow)
        self.actionExit.triggered.connect(lambda: sys.exit(0))

        self.testButton.clicked.connect(self.testButtonPressed)
        self.firstButton.clicked.connect(self.firstButtonPressed)
        self.previousButton.clicked.connect(self.previousButtonPressed)
        self.nextButton.clicked.connect(self.nextButtonPressed)
        self.lastButton.clicked.connect(self.lastButtonPressed)

        self.model=Artist.all()

        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "ID")
        self.model.setHeaderData(1, Qt.Horizontal, "First Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Last Name")
        self.model.select()

        self.tableView.setModel(self.model)
        self.tableView.resizeColumnsToContents()

        self.mapper=QDataWidgetMapper()
        self.mapper.setModel(self.model)
        self.mapper.addMapping(self.firstname, 1)
        self.mapper.addMapping(self.lastname, 2)
        self.mapper.toFirst()

    def firstButtonPressed(self):
        self.mapper.toFirst()

    def previousButtonPressed(self):
        self.mapper.toPrevious()

    def nextButtonPressed(self):
        self.mapper.toNext()

    def lastButtonPressed(self):
        self.mapper.toLast()

    def testButtonPressed(self):

        for i in range(0, self.model.rowCount()):
            first=self.model.record(i).value("first_name")
            last=self.model.record(i).value("last_name")
            print(f"{first}, {last}")