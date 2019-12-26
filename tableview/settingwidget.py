#!/usr/bin/env python3.6
# -*- coding:utf-8 -*-
__author__ = 'Chen_Xa'
__version__ = '1.0'
__date__ = '2019.12.19'
__copyright__ = "Copyright 2019, PI"


import sys
from tableview.ui.form import Ui_Form
from tableview.table_view import MyTableView
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class TableViewWidget(Ui_Form, QWidget):
    def __init__(self):
        super(TableViewWidget, self).__init__()
        self.setupUi(self)
        self.setObjectName("table_view")
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.initView()
        self.connectEvent()

    def initView(self):
        model = QStandardItemModel()
        self.tableView.setModel(model)
        self.tableView.verticalHeader().setVisible(False) # 设置隐藏表格左边垂直
        self.resize(500, 500)

        self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{background:green;}")
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.tableView.setStyleSheet("selection-background-color:lightblue;")

        self.tableView.verticalHeader().setFixedWidth(20)

        self.tableView.horizontalHeader().setSectionsMovable(True);
        self.tableView.horizontalHeader().setDragEnabled(True);
        self.tableView.horizontalHeader().setDragDropMode(QAbstractItemView.InternalMove)

        self.tableView.verticalHeader().setSectionsMovable(True);
        self.tableView.verticalHeader().setDragEnabled(True);
        self.tableView.verticalHeader().setDragDropMode(QAbstractItemView.InternalMove)

    def connectEvent(self):
        self.tableView.changeColsNameSignal.connect(self.onChangeColsName)
        self.tableView.insertColsSignal.connect(self.onInsertCols)
        self.tableView.deleteColsSignal.connect(self.onDeleteCols)
        self.tableView.moveLeftSignal.connect(self.onMoveLeftCols)
        self.tableView.moveRightSignal.connect(self.onMoveRightCols)
        self.file_pushButton.clicked.connect(self.chooseFile)
        self.tableView.clickCellSingle.connect(self.clickCell)

    def clickCell(self, index, action):
        if action.text() == "添加按钮控件":
            pushbutton = QPushButton("button")
            pushbutton.setStyleSheet("QPushButton{""border:3px solid red;""border-radius:5px}")
            self.tableView.setIndexWidget(index, pushbutton)
        elif action.text() == "添加复选框控件":
            checkbox = QCheckBox("checkbox")
            checkbox.setStyleSheet("QCheckBox{""border:3px solid red;""border-radius:5px}")
            self.tableView.setIndexWidget(index, checkbox)

    def chooseFile(self):
        #  读取文件数据动态生成表格
        file_path = QFileDialog.getOpenFileName(self,
                                                    "选择文件",
                                                    "./data",
                                                    "TXT Files(*.txt);;JSON Files(*.json)",
                                                    options=QFileDialog.DontUseNativeDialog)
        if file_path[0] != "":
            self.file_lineEdit.setText(file_path[0])
            with open(file_path[0], "r", encoding='UTF-8') as f:
                for index, line in enumerate(f):
                    for col in range(len(line.strip().split(" "))):
                        self.tableView.model().setItem(index, col, QStandardItem(line.strip().split(" ")[col]))

    def onChangeColsName(self, col):
        col_name, ok = QInputDialog.getText(self, "修改列名", "列名:", QLineEdit.Normal)
        if ok:
            if col_name != "":
                self.tableView.model().setHeaderData(col, Qt.Horizontal, col_name);
            else:
                ok = QMessageBox.warning(self, "错误", "列名不能为空")
                self.onChangeColsName(col)

    def onInsertCols(self, col):
        self.tableView.model().insertColumn(col+1,)

    def onDeleteCols(self, col):
        self.tableView.model().removeColumn(col)

    def onMoveLeftCols(self, col):
        current_index = self.tableView.currentIndex()
        move_to_index = self.tableView.model().index(0, col-1)
        self.tableView.model().moveColumn(current_index, col, move_to_index, col-1)

    def onMoveRightCols(self, col):
        current_index = self.tableView.currentIndex()
        move_to_index = self.tableView.model().index(0, col+1)
        self.tableView.model().moveColumn(current_index, col+1, move_to_index, col)


# if __name__ == "__main__":
#     widget = SettingWidget()
#     widget.show()
#     sys.exit(app.exec())
