'''
Created on 24/07/2013

@author: ruben
'''
from PyQt4.QtGui import QFileDialog
from PyQt4.QtCore import QRegExp
from PyQt4.QtCore import QFile
from PyQt4.QtCore import QDir
from PyQt4.QtCore import QTextStream
from PyQt4.QtCore import QIODevice
from PyQt4.QtCore import QTime
import base64



class Guardar(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cadenaAguardar = ""
        self.tiempo = QTime()
        self.nombre = ""
        self.nivel = ""
        self.matriz = [ [ 0 for i in range(9) ] for j in range(9) ]
        self.solucion = [ [ 0 for i in range(9) ] for j in range(9) ]

    def crearArchivo(self):
        dialog = QFileDialog(None)
        dialog.setFileMode(0)
        dialog.setDefaultSuffix("su")
        pathInicial = QDir.homePath() + "/untitled.su"
        nombre = dialog.getSaveFileName(None, "Save As", pathInicial, "Sudoku (*.su)")
        if nombre == None:
            return False
        else:
            file = open("out.txt", "w")
            file.write(self.cadenaAguardar)
            file.close()
            base64.encode(open("out.txt"), open(nombre, "w"))
            print "se creo archivo"
            return True
            
    def guardarValores(self, matriz, solucion, nombre, nivel, tiempo):
        #concateno string de la solucion
        for i in range(0,9):
            for j in range(0,9):
                tmp = solucion[i][j]
                self.cadenaAguardar = self.cadenaAguardar + str(tmp)
        #concateno el string del tablero actual de juego
        self.cadenaAguardar = self.cadenaAguardar + "^"
        for i in range(0,9):
            for j in range(0,9):
                tmp = matriz[i][j]
                self.cadenaAguardar = self.cadenaAguardar + str(tmp)
        self.cadenaAguardar = self.cadenaAguardar + "^"
        #concateno el nombre del jugador
        self.cadenaAguardar = self.cadenaAguardar + nombre + "^"
        #concateno el nivel del jugador
        self.cadenaAguardar = self.cadenaAguardar + nivel + "^"
        #concateno el tiempo de juego
        self.cadenaAguardar = self.cadenaAguardar + tiempo
        print self.cadenaAguardar
        
    def leerArchivo(self):
        nombre = QFileDialog.getOpenFileName(None, "Abrir archivo", QDir.homePath(), "*.su")
        print nombre
        if nombre == None:
            return False
        else:
            k = 0
            print "entro al if archivo.open"
            base64.decode(open(nombre), open("out.txt", "w"))
            print "imprimiendo cadena leida"
      
            print "imprimiendo cadena decodificada"
            data = open("out.txt").read()
            print "decoded message:", data
            #Aqui debe ir la parte de descriptacion
            
            lista = data.split("^")
            print lista
            #setenado matriz de juego actual y solucion
            actual = lista[0] #cadena con matriz de juego actual
            actual2 = lista[1] #cadena con solucion
            for i in range(0,9):
                for j in range(0,9):
                    tmp = int(actual[k])
                    tmp2 = int(actual2[k])
                    self.matriz[i][j] = tmp
                    self.solucion[i][j] = tmp2
                    k = k + 1
            #seteando nombre del jugador
            self.nombre = lista[2]
            #setenado nivel de juego
            self.nivel = lista[3]
            #seteando objeto tiempo de juego
            actual = lista[4]
            listaHMS = actual.split(":")
            h = listaHMS[0]
            m = listaHMS[1]
            s = listaHMS[2]
            self.tiempo.setHMS(int(h), int(m), int(s))
            print self.matriz
            print self.solucion
            print self.nombre
            print self.nivel
            print self.tiempo
            return True
        
        
