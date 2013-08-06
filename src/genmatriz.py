'''
Created on 21/07/2013

@author: ruben
'''
from random import randint

class GenMatriz(object):
    '''
    classdocs
    '''
    matriz = [ [ 0 for i in range(9) ] for j in range(9) ]
    matrizSemilla = [ [ 0 for i in range(9) ] for j in range(9) ]
    uno = []
    dos = []
    tres = []
    cuatro = []
    cinco = []
    seis = []
    siete = []
    ocho = []
    nueve = []
    
    def __init__(self):
        '''
        Constructor
        '''
        self.llenarMatrizSemilla()
        self.generarArreglos()
        self.generarMatrizSudoku()
        
    def llenarMatrizSemilla(self):
        k =0
        valores = [2,7,1,6,3,4,8,5,9,
                   5,6,9,8,2,7,3,1,4,
                   4,3,8,1,5,9,6,2,7,
                   6,8,2,5,4,1,7,9,3,
                   1,9,4,2,7,3,5,8,6,
                   7,5,3,9,6,8,2,4,1,
                   8,1,7,3,9,2,4,6,5,
                   9,4,6,7,8,5,1,3,2,
                   3,2,5,4,1,6,9,7,8]
        #cargar valores de la matriz semilla del algoritmo
        for j in range(0,9):
            for l in range(0,9):
                self.matrizSemilla[j][l] = valores[k]
                k = k+1
        print self.matrizSemilla
        
    def generarMatrizSudoku(self):
        aleatorio = 0
        tmp =0
        tmp2 = 8
        numero = [1,2,3,4,5,6,7,8,9]
        aleatorios = []
        for i in range(0,9):
            aleatorio = randint(0,tmp2)
            print "rand: " + str(aleatorio)
            tmp = numero.pop(aleatorio)
            aleatorios.append(tmp)
            tmp2 = tmp2 -1
        self.colocarNumeros(aleatorios)
        print aleatorios
        
    def generarArreglos(self):
        tmp =0
        for i in range(0,9):
            for j in range(0,9):
                tmp = self.matrizSemilla[i][j]
                self.guardarPosNum(tmp, i, j)
                
    def guardarPosNum(self, num, fila, columna):
        if num==1:
            poscicion = [fila, columna]
            self.uno.append(poscicion)
        if num==2:
            poscicion = [fila, columna]
            self.dos.append(poscicion)
        if num==3:
            poscicion = [fila, columna]
            self.tres.append(poscicion)
        if num==4:
            poscicion = [fila, columna]
            self.cuatro.append(poscicion)
        if num==5:
            poscicion = [fila, columna]
            self.cinco.append(poscicion)
        if num==6:
            poscicion = [fila, columna]
            self.seis.append(poscicion)
        if num==7:
            poscicion = [fila, columna]
            self.siete.append(poscicion)
        if num==8:
            poscicion = [fila, columna]
            self.ocho.append(poscicion)
        if num==9:
            poscicion = [fila, columna]
            self.nueve.append(poscicion)
            
    '''Para obtener numeros de la poscicion tenemos que poner obtener el arreglo poscicion
    y luego indicar [0]=>fila, [1]=>columna '''
    def colocarNumeros(self, aleatorios):
        tmp = 0
        fila = 0
        columna = 0
        tmp2 = 1
        for i in range(0,9):
            tmp = aleatorios[i]
            if tmp2 == 1:
                for j in range(0,9):
                    fila = self.uno[j][0]
                    columna = self.uno[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 2:
                for j in range(0,9):
                    fila = self.dos[j][0]
                    columna = self.dos[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 3:
                for j in range(0,9):
                    fila = self.tres[j][0]
                    columna = self.tres[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 4:
                for j in range(0,9):
                    fila = self.cuatro[j][0]
                    columna = self.cuatro[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 5:
                for j in range(0,9):
                    fila = self.cinco[j][0]
                    columna = self.cinco[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 6:
                for j in range(0,9):
                    fila = self.seis[j][0]
                    columna = self.seis[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 7:
                for j in range(0,9):
                    fila = self.siete[j][0]
                    columna = self.siete[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 8:
                for j in range(0,9):
                    fila = self.ocho[j][0]
                    columna = self.ocho[j][1]
                    self.matriz[fila][columna] = tmp
            if tmp2 == 9:
                for j in range(0,9):
                    fila = self.nueve[j][0]
                    columna = self.nueve[j][1]
                    self.matriz[fila][columna] = tmp
            tmp2 = tmp2 +1
        print self.matriz
        
        
            
                    
            
                    
        

        
        
            
        