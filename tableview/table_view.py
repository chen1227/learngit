# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 20:38
# @Author  : chen_xa
# @Email   : 768577220@qq.com


from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MyTableView(QTableView):
    insertColsSignal = pyqtSignal(int)
    deleteColsSignal = pyqtSignal(int)
    changeColsNameSignal = pyqtSignal(int)
    changeRowsNameSignal = pyqtSignal(int)
    moveLeftSignal = pyqtSignal(int)
    moveRightSignal = pyqtSignal(int)
    insertRowsSignal = pyqtSignal(int)
    moveUpSignal = pyqtSignal(int)
    moveDownSignal = pyqtSignal(int)
    deleteRowsSignal = pyqtSignal(int)
    clickCellSingle = pyqtSignal(QModelIndex, QAction)

    def __init__(self, parent):
        super(MyTableView, self).__init__(parent)
        self.creatAction()
        self.horizontalHeader().sectionPressed.connect(self.onColClick)
        self.clicked.connect(self.onClickCell) # 单元格被点击的信号

    def creatAction(self):
        self.insert_rows = QAction(self.tr("插入行"))
        self.insert_clos = QAction(self.tr("插入列"))
        self.change_cols_name = QAction(self.tr("修改列名"))
        self.change_rows_name = QAction(self.tr("修改行名"))
        self.move_up = QAction(self.tr("上移"))
        self.move_down = QAction(self.tr("下移"))
        self.move_right = QAction(self.tr("右移"))
        self.move_left = QAction(self.tr("左移"))
        self.delete_cols = QAction(self.tr("删除列"))
        self.delete_rows = QAction(self.tr("删除行"))

    def onColClick(self, col):
        menu = QMenu()
        menu.addAction(self.insert_clos)
        menu.addAction(self.change_cols_name)
        menu.addAction(self.move_left)
        menu.addAction(self.move_right)
        menu.addAction(self.delete_cols)
        self.insert_clos.triggered.connect(lambda : self.onActionInsertCols(col))
        self.change_cols_name.triggered.connect(lambda : self.onActionChangeColsName(col))
        self.move_left.triggered.connect(lambda : self.onActionMoveLeft(col))
        self.move_right.triggered.connect(lambda : self.onActionMoveRight(col))
        self.delete_cols.triggered.connect(lambda : self.onActionDeleteCols(col))
        menu.exec_(QCursor.pos())
        self.insert_clos.triggered.disconnect()
        self.change_cols_name.triggered.disconnect()
        self.move_left.triggered.disconnect()
        self.move_right.triggered.disconnect()
        self.delete_cols.triggered.disconnect()

    def onActionInsertCols(self, col):
        self.insertColsSignal.emit(col)

    def onActionChangeColsName(self, col):
        self.changeColsNameSignal.emit(col)

    def onActionMoveLeft(self, col):
        self.moveLeftSignal.emit(col)

    def onActionMoveRight(self, col):
        self.moveRightSignal.emit(col)

    def onActionDeleteCols(self, col):
        self.deleteColsSignal.emit(col)

    def onClickCell(self, index):
        item = self.model().itemFromIndex(index)
        if item.text() == "":
            menu = QMenu()
            add_pushbutton_action = QAction("添加按钮控件")
            add_checkbox_action = QAction("添加复选框控件")

            menu.addAction(add_pushbutton_action)
            menu.addAction(add_checkbox_action)
            add_pushbutton_action.triggered.connect(lambda: self.onActionClickCell(index))
            add_checkbox_action.triggered.connect(lambda: self.onActionClickCell(index))

            menu.exec_(QCursor.pos())
            add_pushbutton_action.triggered.disconnect()
            add_checkbox_action.triggered.disconnect()

    def onActionClickCell(self, index):
        self.clickCellSingle.emit(index, self.sender())

