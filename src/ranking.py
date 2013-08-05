'''
Created on 25/07/2013

@author: jegerima
'''
from PyQt4 import QtGui
from PyQt4 import QtCore
from ui_ranking import Ui_Ranking

class Ranking(QtGui.QDialog):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        QtCore.QObject.__init__(self)
        self.ui=Ui_Ranking()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        
    def on_cmd_ok_clicked(self):
        self.close()
        self.destroy()
