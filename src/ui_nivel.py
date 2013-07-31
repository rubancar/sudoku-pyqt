# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nivel.ui'
#
# Created: Tue Jul 30 14:09:13 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_nivel(object):
    def setupUi(self, nivel):
        nivel.setObjectName(_fromUtf8("nivel"))
        nivel.setWindowModality(QtCore.Qt.WindowModal)
        nivel.resize(360, 358)
        nivel.setWindowTitle(_fromUtf8("QSudoku - Niveles"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Recursos/i160x130.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        nivel.setWindowIcon(icon)
        nivel.setAutoFillBackground(False)
        self.verticalLayoutWidget = QtGui.QWidget(nivel)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 150, 160, 191))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.lyLevel = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.lyLevel.setMargin(0)
        self.lyLevel.setObjectName(_fromUtf8("lyLevel"))
        self.label = QtGui.QLabel(nivel)
        self.label.setGeometry(QtCore.QRect(70, 120, 231, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(nivel)
        self.label_2.setGeometry(QtCore.QRect(20, -10, 321, 121))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/Recursos/icon640.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(nivel)
        QtCore.QMetaObject.connectSlotsByName(nivel)

    def retranslateUi(self, nivel):
        self.label.setText(QtGui.QApplication.translate("nivel", "Seleccione un nivel de dificultad:", None, QtGui.QApplication.UnicodeUTF8))

import images
