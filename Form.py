# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 300)

        self.label = QtWidgets.QTextEdit(Form)
        self.label.setGeometry(QtCore.QRect(21, 180, 380, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        # self.label.focusProxy()

        # self.label = QtWidgets.QLabel(Form)
        # self.label.setGeometry(QtCore.QRect(21, 53, 231, 16))
        # self.label.setText("")
        # self.label.setObjectName("label")

        # QtWidgets.QLineEdit
        # aaa = QtWidgets.QPlainTextEdit(Form)
        # bbb = QtWidgets.QLineEdit(Form)
        # bbb.text()
        # aaa.text()
        # aaa.getPaintContext()
        self.lineEdit = QtWidgets.QPlainTextEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(21, 33, 380, 100))
        self.lineEdit.setPlainText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText('请粘贴分享的内容')

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(410, 93, 50, 40))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # self.lineEdit = QtWidgets.QLineEdit(self.widget)
        # self.lineEdit.setObjectName("lineEdit")

        # self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.run)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "抖音无水印下载"))
        self.pushButton.setText(_translate("Form", "下载"))


