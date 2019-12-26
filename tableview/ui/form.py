# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(471, 698)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 451, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.file_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_pushButton.setObjectName("file_pushButton")
        self.gridLayout.addWidget(self.file_pushButton, 0, 1, 1, 1)
        self.file_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.file_lineEdit.setObjectName("file_lineEdit")
        self.gridLayout.addWidget(self.file_lineEdit, 0, 0, 1, 1)
        self.floder_lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.floder_lineEdit.setObjectName("floder_lineEdit")
        self.gridLayout.addWidget(self.floder_lineEdit, 1, 0, 1, 1)
        self.floder_pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.floder_pushButton.setObjectName("floder_pushButton")
        self.gridLayout.addWidget(self.floder_pushButton, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableView = MyTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.file_pushButton.setText(_translate("Form", "确认"))
        self.floder_pushButton.setText(_translate("Form", "确认"))


from tableview.table_view import MyTableView
