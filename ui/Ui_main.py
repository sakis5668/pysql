# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/sakis/Documents/git/pysql/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setGeometry(QtCore.QRect(60, 10, 80, 23))
        self.testButton.setObjectName("testButton")
        self.firstname = QtWidgets.QLineEdit(self.centralwidget)
        self.firstname.setGeometry(QtCore.QRect(60, 90, 201, 23))
        self.firstname.setObjectName("firstname")
        self.lastname = QtWidgets.QLineEdit(self.centralwidget)
        self.lastname.setGeometry(QtCore.QRect(60, 120, 201, 23))
        self.lastname.setObjectName("lastname")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(60, 160, 451, 192))
        self.tableView.setObjectName("tableView")
        self.firstButton = QtWidgets.QPushButton(self.centralwidget)
        self.firstButton.setGeometry(QtCore.QRect(60, 50, 21, 23))
        self.firstButton.setObjectName("firstButton")
        self.previousButton = QtWidgets.QPushButton(self.centralwidget)
        self.previousButton.setGeometry(QtCore.QRect(90, 50, 21, 23))
        self.previousButton.setObjectName("previousButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(120, 50, 21, 23))
        self.nextButton.setObjectName("nextButton")
        self.lastButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastButton.setGeometry(QtCore.QRect(150, 50, 21, 23))
        self.lastButton.setObjectName("lastButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.firstButton.setText(_translate("MainWindow", "<<"))
        self.previousButton.setText(_translate("MainWindow", "<"))
        self.nextButton.setText(_translate("MainWindow", ">"))
        self.lastButton.setText(_translate("MainWindow", ">>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
