#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
__author__ = 'Chen_Xa'
__version__ = '1.0'
__date__ = '2019.12.19'
__copyright__ = "Copyright 2019, PI"


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from ui.mainwindow import Ui_MainWindow
app = QApplication(sys.argv)


class Demo(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)

        self.setWindowTitle("PyQt5学习")
        self.initView()
        self.initMenu()

    def initView(self):
        self.tabWidget.setTabText(0, "QTableView学习")
        self.tabWidget.setTabText(1, "QTreeView学习")

    def initMenu(self):
        menubar = self.menuBar.addMenu("菜单")
        menubar.addAction("运行")


if __name__ == "__main__":
    window = Demo()
    window.show()
    sys.exit(app.exec())