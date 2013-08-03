'''
Created on 24/07/2013

@author: CesarM
'''
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Celda(QFrame):
    '''
    classdocs
    '''


    def __init__(self, fila, columna, valor):
        '''
        Constructor
        '''
        QFrame.__init__(self)
        self.qv = QVBoxLayout(self)
        self.qv.setMargin(0)
        self.qv.setSpacing(0)
        self.valor = valor
        self.fila = fila
        self.columna = columna
        
        #numero principal
        f1 = QFont("Arial", 16, 1)
        self.number = QLabel(str(valor))
        self.number.setFont(f1)
        self.number.setAlignment(Qt.AlignCenter)
        self.qv.addWidget(self.number)
        
        #numero potencial
        self.little_number = QLabel("")
        self.little_number.setLineWidth(1)
        self.little_number.setAlignment(Qt.AlignCenter)
        self.little_number.setFrameShape(QFrame.Box)
        
        #sugerencias de numeros
        f3 = QFont("Arial", 8)
        self.hints = QLabel("")
        self.hints.setFont(f3)
        self.hints.setAlignment(Qt.AlignCenter)
        self.hints.setLineWidth(1)
        self.hints.setFrameShape(QFrame.Box)
        
        #opciones del frame
        grid = QGridLayout()
        grid.addWidget(self.hints,0,0,0,3)
        grid.addWidget(self.little_number,0,3,1,1)
        self.qv.addLayout(grid,0)
        self.setLayout(self.qv)
        self.setLineWidth(2)
        self.setFrameShape(QFrame.Box)
        self.paleta = QPalette()
        self.paleta.setColor(QPalette.Foreground, Qt.black)
        self.setPalette(self.paleta)
        
    def getValue(self):
        print self.valor
        return self.valor
   
    def setValue(self, valor):
        if valor == 0:
            self.valor = valor
            self.number.setText("")
        else:
            self.valor = valor
            self.paleta.setColor(QPalette.Foreground, Qt.black)
            self.setPalette(self.paleta)
            self.number.setText(str(self.valor))
            
    def setEmpty(self):
        print "entra a cambiar el color... :)"
        self.paleta.setColor(QPalette.Foreground, Qt.blue)
        self.setPalette(self.paleta)
        self.setBackColor("white")
        
    def reset(self):
        self.little_number.setText("")
        self.hints.setText("")
        
    def setBlackBorder(self):
        self.paleta.setColor(QPalette.Foreground, Qt.black)
        self.setPalette(self.paleta)
    
    def mouseReleaseEvent(self, event):
        self.emit(SIGNAL("clicked()"))
        
    def setBackColor(self, color):
        self.number.setStyleSheet("QLabel { background-color: " + color + "; }")
        
    def addHints(self, valor):
        tmp2 = self.hints.text()
        if tmp2 != "":
            tmp = int(tmp2)
            self.hints.setText(str(tmp*10+valor))
        else:
            tmp = 0
            self.hints.setText(str(tmp*10+valor))
        
        
        
