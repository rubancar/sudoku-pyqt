# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ranking.ui'
#
# Created: Sat Jul 27 21:04:59 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Ranking(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(348, 443)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 321, 101))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/Recursos/340x120.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 301, 261))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cmd_ok = QtGui.QPushButton(Form)
        self.cmd_ok.setGeometry(QtCore.QRect(130, 390, 90, 27))
        self.cmd_ok.setObjectName(_fromUtf8("cmd_ok"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Ranking", None, QtGui.QApplication.UnicodeUTF8))
        self.cmd_ok.setText(QtGui.QApplication.translate("Form", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

import images
