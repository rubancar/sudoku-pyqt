# Form implementation generated from reading ui file 'about.ui'
#
# Created: Fri Jul 26 14:08:32 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_about(object):
    def setupUi(self, about):
        about.setObjectName(_fromUtf8("about"))
        about.resize(320, 240)
        self.lbl_espol = QtGui.QLabel(about)
        self.lbl_espol.setGeometry(QtCore.QRect(220, 100, 80, 80))
        self.lbl_espol.setText(_fromUtf8(""))
        self.lbl_espol.setPixmap(QtGui.QPixmap(_fromUtf8(":/Recursos/espol.gif")))
        self.lbl_espol.setScaledContents(True)
        self.lbl_espol.setObjectName(_fromUtf8("lbl_espol"))
        self.lbl_logo = QtGui.QLabel(about)
        self.lbl_logo.setGeometry(QtCore.QRect(10, -10, 291, 111))
        self.lbl_logo.setText(_fromUtf8(""))
        self.lbl_logo.setPixmap(QtGui.QPixmap(_fromUtf8(":/Recursos/icon640.png")))
        self.lbl_logo.setScaledContents(True)
        self.lbl_logo.setObjectName(_fromUtf8("lbl_logo"))
        self.label = QtGui.QLabel(about)
        self.label.setGeometry(QtCore.QRect(20, 110, 161, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(about)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 121, 17))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(about)
        self.label_3.setGeometry(QtCore.QRect(40, 170, 121, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(about)
        self.label_4.setGeometry(QtCore.QRect(40, 190, 121, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(about)
        self.pushButton.setGeometry(QtCore.QRect(210, 200, 99, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(about)
        QtCore.QMetaObject.connectSlotsByName(about)

    def retranslateUi(self, about):
        about.setWindowTitle(QtGui.QApplication.translate("about", "Acerca de", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("about", "QSudoku Version 1.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("about", "Jefferson Rivera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("about", "Ruben Carvajal", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("about", "Cesar Madrid", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("about", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))

import images
