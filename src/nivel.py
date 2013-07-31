'''
Created on 30/07/2013

@author: CesarM
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from ui_nivel import Ui_nivel

class Nivel(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtCore.QObject.__init__(self)
        self.ui=Ui_nivel()
        self.ui.setupUi(self)
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.initGui()
        
    def initGui(self):
        
        #botones de eleccion
        self.levels = []
        self.levels.append(QtGui.QPushButton("Novato"))
        self.levels.append(QtGui.QPushButton("Intermedio"))
        self.levels.append(QtGui.QPushButton("Profesional"))
        self.levels.append(QtGui.QPushButton("Leyenda"))
        
        #conectando eventos
        for i in range(0,4):
            QtCore.QObject.connect(self.levels[i], QtCore.SIGNAL("clicked()"), self.appReady)
            self.ui.lyLevel.addWidget(self.levels[i])
            
        self.setFixedSize(self.size())
        
    def appReady(self):
        cmd = self.sender()
        if cmd.text() == "Novato":
            self.emit(QtCore.SIGNAL("nivel"), 0)
        if cmd.text() == "Intermedio":
            self.emit(QtCore.SIGNAL("nivel"), 1)
        if cmd.text() == "Profesional":
            self.emit(QtCore.SIGNAL("nivel"), 2)
        if cmd.text() == "Leyenda":
            self.emit(QtCore.SIGNAL("nivel"), 3)
    
            
            
        
        
        
