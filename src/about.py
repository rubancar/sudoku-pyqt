'''
Created on 25/07/2013

@author: jegerima
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from ui_about import Ui_about

class About(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtCore.QObject.__init__(self)
        self.ui=Ui_about()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        
    def on_pushButton_clicked(self):
        self.close()
        self.destroy()
