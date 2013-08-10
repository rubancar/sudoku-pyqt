import sys
 
# Import Qt modules
from PyQt4 import QtGui
from PyQt4.QtCore import *
from maintable import Ui_MainTable
from celda import Celda
from nivel import Nivel
from genmatriz import GenMatriz
from random import randint
from guardar import Guardar
from about import About
from ranking import Ranking

 
# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QObject.__init__(self)
        self.cuadros = []
        self.casillas = []
        QtGui.QMainWindow.__init__(self)
        QtGui.QMessageBox.information(self, "Bienvenido a sudoku", "Bienvenido a QSudoku. Version 0.2.05")
        self.ui=Ui_MainTable()
        self.ui.setupUi(self)
        self.initGuiCelda()
        self.initMenuBar()
        self.initTeclado()
                
        #formulario de niveles
        self.level = Nivel()
        QObject.connect(self.level, SIGNAL("nivel"), self.iniciarJuego)
        self.ui.crono.display("00:00")
        self.bandera = True
        
        
    def initGuiCelda(self):
        self.ui.cmdVerificar.setEnabled(False)
        self.ui.cmdHint.setEnabled(False)
        self.ui.tablero.setHorizontalSpacing(8)
        self.ui.tablero.setVerticalSpacing(8)
        self.casillas = []
        z=0
        fil = 0
        col = 0
        for i in range(0,3):
            fil = i*3
            for j in range(0,3):
                col = j*3
                cuadro = QtGui.QGridLayout()
                cuadro.setHorizontalSpacing(1)
                cuadro.setVerticalSpacing(1)
                for l in range(0,3):
                    for m in range(0,3):
                        cas = Celda(fil, col, 0)
                        self.casillas.append(cas)
                        cuadro.addWidget(cas,l,m)
                        z = z+1
                        col = col +1
                    fil = fil +1
                    col = j*3
                self.ui.tablero.addLayout(cuadro, i, j)
                fil = i*3
        self.celdaRuntime = Celda(0,0,0)
        self.tm = QTime(0,0,0,0)
        
                
    def initCrono(self):
        self.tiempo = QTimer(self)
        QObject.connect(self.tiempo, SIGNAL("timeout()"), self.timeRefresh)
        self.tiempo.start(1000)
        self.tiempoIni = QTime.currentTime()
        QTimer.singleShot(1000, self.timeRefresh)
        
    def timeRefresh(self):
        actual = QTime.currentTime()
        m_ini = self.tiempoIni.minute()
        s_ini = self.tiempoIni.second()
        ms_ini = self.tiempoIni.msec()
        m_act = actual.minute()
        s_act = actual.second()
        ms_act = actual.msec()
        
        if ms_act < ms_ini:
            ms_act = 1000 + ms_act
            s_act = s_act +1
        if s_act < s_ini:
            s_act = 60 + s_act
            m_act = m_act - 1
            
        m = m_act - m_ini
        s = s_act - s_ini
        ms = ms_act - ms_ini
        #actualizo el tiempo
        
        self.tm.setHMS(0, m, s, ms)
        self.ui.crono.display(self.tm.toString("mm:ss")) 
    
    def initMenuBar(self):
        QObject.connect(self.ui.actionAcerca_de, SIGNAL("triggered()"), self.acercaDe)
        QObject.connect(self.ui.actionNueva, SIGNAL("triggered()"), self.nuevaPartida)
        QObject.connect(self.ui.actionGuardar, SIGNAL("triggered()"), self.guardarPartida)
        QObject.connect(self.ui.actionCargar, SIGNAL("triggered()"), self.cargarPartida)
        QObject.connect(self.ui.actionSalir, SIGNAL("triggered()"), self.salirJuego)
        QObject.connect(self.ui.actionRanking, SIGNAL("triggered()"), self.verRanking)
        
    def verRanking(self):
        self.ranking = Ranking()
        self.ranking.setWindowModality(Qt.ApplicationModal)
        self.ranking.show()
        
    
    def salirJuego(self):
        puntaje = self.calcularPuntaje()
        QtGui.QMessageBox.about(self, "Salir", "Su puntaje fue de : "+ str(puntaje))
        self.close()
        self.destroy()
    
    def acercaDe(self):
        print "entra a acerca de :)"
        self.ab = About()
        self.ab.setWindowModality(Qt.ApplicationModal)
        self.ab.show()

    def nuevaPartida(self):
        self.level.show()
    
       
    def iniciarJuego(self, nivel):
        self.level.hide()
        self.activarTeclado()
        self.setCeldasBlanco()
        self.setTableroInicio()
        self.setTableroInicialSegunNivel(nivel)
        self.setTableroEnPantalla()
        while True:
            self.nombre, valor = QtGui.QInputDialog.getText(self, "Sudoku", "Ingrese su nombre")
            if self.nombre == "" or valor==False:
                QtGui.QMessageBox.warning(self, "Mensaje", "No se ha ingresado texto")
            else:
                break
        self.ui.lbl_jugador.setText(self.nombre)
        if nivel==0:
            self.ui.lbl_level.setText("Novato")
            self.hints = 12
            self.dificultad = 0
        elif nivel==1:
            self.ui.lbl_level.setText("Intermedio")
            self.hints = 8
            self.dificultad = 1
        elif nivel==2:
            self.ui.lbl_level.setText("Profesional")
            self.hints = 4
            self.dificultad = 2
        elif nivel==3:
            self.ui.lbl_level.setText("Leyenda")
            self.hints = 2
            self.dificultad = 3
        self.initCrono()
        self.ui.cmdHint.setText("Hints "+str(self.hints))
        
    def setTableroEnPantalla(self):
        for i in range(0,9):
            for j in range(0,9):
                tmp = self.tableroActual[i][j]
                if tmp!= 0:
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setValue(tmp)
                else:
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setValue(0)
                    
        
    def setTableroInicialSegunNivel(self, nivel):
        if nivel==0:
            for i in range(0,50):
                fila = randint(0,8)
                col = randint(0,8)
                self.tableroActual[fila][col] = self.matriz[fila][col]
                
        if nivel==1:
            for i in range(0,40):
                fila = randint(0,8)
                col = randint(0,8)
                self.tableroActual[fila][col] = self.matriz[fila][col]
            
        if nivel==2:
            for i in range(0,30):
                fila = randint(0,8)
                col = randint(0,8)
                self.tableroActual[fila][col] = self.matriz[fila][col]
                
        if nivel==3:
            for i in range(0,25):
                fila = randint(0,8)
                col = randint(0,8)
                self.tableroActual[fila][col] = self.matriz[fila][col]    
        print self.tableroActual
        
        
    def setTableroInicio(self):
        matrizSolucion = GenMatriz()
        self.matriz = [ [ 0 for i in range(9) ] for j in range(9) ]
        self.tableroActual = [ [ 0 for i in range(9) ] for j in range(9) ]
        self.matriz = matrizSolucion.matriz
        print "imprimiendo matriz de juego main: \n" 
        print self.matriz
            
        
    def setCeldasBlanco(self):
        for i in range(0,9):
            for j in range(0,9):
                self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("white")
        
        
    def activarTeclado(self):
        for i in range(0,10):
            self.teclado[i].setEnabled(True)
        self.ui.cmdHint.setEnabled(True)
        self.ui.cmdVerificar.setEnabled(True)
        QObject.connect(self.ui.cmdHint, SIGNAL("clicked()"), self.cmdHint_clicked)
        QObject.connect(self.ui.cmdVerificar, SIGNAL("clicked()"), self.cmdVerificar_clicked)
        for i in range(0,81):
            cas = self.casillas[i]
            QObject.connect(cas, SIGNAL("clicked()"), cas.setEmpty)
            QObject.connect(cas, SIGNAL("clicked()"), self.getCeldaRuntime)
        
        
    def initTeclado(self):
        z=0
        self.teclado = []
        for i in range(0,3):
            for j in range(0,3):
                cmd = QtGui.QPushButton(str(z+1))
                cmd.setEnabled(False)
                self.teclado.append(cmd)
                QObject.connect(self.teclado[z], SIGNAL("clicked()"), self.numPressed)
                print "entra "+str(z)
                self.ui.tecladoNum.addWidget(self.teclado[z],i,j)
                z = z+1
        cmd = QtGui.QPushButton("0")
        cmd.setEnabled(False)
        self.teclado.append(cmd)
        QObject.connect(self.teclado[z], SIGNAL("clicked()"), self.numPressed)
        self.ui.tecladoNum.addWidget(self.teclado[z], 4, 1)
    
    def numPressed(self):
        numeroASetear = int(self.sender().text())
        self.celdaRuntime.setValue(numeroASetear)
        
    def getCeldaRuntime(self):
        if self.celdaRuntime:
            print "entra a resetear y colocar borde"
            self.celdaRuntime.reset()
            self.celdaRuntime.setBlackBorder()
        if self.bandera == False:
            self.volverTableroNormal()
            self.bandera = True
        self.celdaRuntime = self.sender()
        self.setTableroActual()
        self.setPistas()
        
    def setTableroActual(self):
        print "dentro de setTableroActual"
        try:
            print self.tableroActual
            for i in range(0,9):
                for j in range(0,9):
                    tmp = self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().getValue()
                    self.tableroActual[i][j] = tmp
        except AttributeError:
            print "Aun no se inicializado tableroActual... :("
        
        
    def setPistas(self):
        pistas = [1,2,3,4,5,6,7,8,9]
        fila = self.celdaRuntime.fila
        columna = self.celdaRuntime.columna
        print "fila: " +str(fila) + "columna: " +str(columna)
        print "pista en fila"
        try:
            for i in range(0,9):
                tmp = self.tableroActual[fila][i]
                print tmp
                if tmp!=0:
                    pistas[tmp-1]=0
            print "pista en columna"
            for j in range(0,9):
                tmp = self.tableroActual[j][columna]
                print tmp
                if tmp!= 0:
                    pistas[tmp-1]=0
            l = (((columna/3)+1)+(fila/3)*3)
            for i in range((((l-1)/3)*3),((((l-1)/3)*3)+3)):
                for j in range((((l-1)%3)*3),((((l-1)%3)*3)+3)):
                    tmp = self.tableroActual[i][j]
                    if tmp != 0:
                        pistas[tmp-1]=0
                    
        except AttributeError:
            print "Aun no se inicializado tableroActual... :("
        k = 0
        print "pistas: "
        print pistas
        for j in range(0,9):
            tmp = pistas[j]
            if tmp!=0 & k<5:
                self.celdaRuntime.addHints(tmp)
                k = k+1
                
    def guardarPartida(self):
        g = Guardar()
        try:
            self.setTableroActual()
            g.guardarValores(self.matriz, self.tableroActual, self.nombre, self.ui.lbl_level.text(), self.tm.toString())
            if g.crearArchivo() == True:
                print "se creo archivo"
            else:
                print "cancelo o ocurrio algun error :("
        except AttributeError:
            print "no ha empezado a jugar..."
            QtGui.QMessageBox.about(self, "Mensaje", "Aun no has empezado a jugar...  intentalo   :)")
        
        
    
    def cargarPartida(self):
        g = Guardar()
        if g.leerArchivo() == True:
            self.tableroActual = g.matriz
            self.matriz = g.matriz
            self.nombre = g.nombre
            self.ui.lbl_jugador.setText(g.nombre)
            self.ui.lbl_level.setText(g.nivel)
            self.setTableroEnPantalla()
            self.activarTeclado()
            self.setCeldasBlanco()
            self.initCrono()
        else:
            return
        
    def checkFila(self, fila, col):
        for i in range(0,9):
            if i!=col:
                if self.tableroActual[fila][i] == self.tableroActual[fila][col]:
                    print "Error en fila "+str(fila+1)
                    return False
        return True
    
    def checkColumna(self, fila, col):
        for i in range(0,9):
            if i!=fila:
                if self.tableroActual[i][col] == self.tableroActual[fila][col]:
                    print "Error en la columna " + str(col+1)
                    return False
        return True
    
    def chechCuadro(self, fila, col):
        v_cuadro = int(fila/3)
        h_cuadro = int(col/3)
        for i in range(v_cuadro*3,v_cuadro*3+3):
            for j in range(h_cuadro*3,h_cuadro*3+3):
                if i != fila or j != col:
                    if self.tableroActual[fila][col] == self.tableroActual[i][j]:
                        print "Error en el cuadro: "+str(fila)+","+str(col)
                        return False
        return True
    
    def cmdVerificar_clicked(self):
        t = True
        self.setTableroActual()
        for i in range(0,9):
            for j in range(0,9):
                self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("white")
                if self.checkFila(i, j)==False:
                    #pintar las celdas de Rojo
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("red")
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBlackBorder()
                    t = False
                if self.checkColumna(i, j)==False:
                    #pintar las celdas de rojo
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("red")
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBlackBorder()
                    t = False
                if self.chechCuadro(i, j)==False:
                    #pintar las celdas de rojo
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("red")
                    self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBlackBorder()
                    t = False
        if t==True:
            QtGui.QMessageBox.about(self, "Felicitaciones", "Sudoku Resuleto Correctamente")
        else:
            QtGui.QMessageBox.about(self, "Mensaje", "Sudoku resuleto incorrectamente")
        self.bandera = False


    def volverTableroNormal(self):
        for i in range(0,9):
            for j in range(0,9):
                self.ui.tablero.itemAtPosition(i/3, j/3).itemAtPosition(i%3, j%3).widget().setBackColor("white")
        
    def cmdHint_clicked(self):
        print "proximamente lo implementaremos"
        if self.hints > 0:
            self.hints = self.hints-1
            self.sender().setText("Hints "+str(self.hints))
            self.setTableroActual()
            while True:
                irnd = randint(1,8)
                jrnd = randint(1,8)
                if self.tableroActual[irnd][jrnd] == 0:
                    break
            self.tableroActual[irnd][jrnd] = self.matriz[irnd][jrnd]
            self.ui.tablero.itemAtPosition(irnd/3, jrnd/3).itemAtPosition(irnd%3, jrnd%3).widget().setValue(self.tableroActual[irnd][jrnd])
            self.setTableroEnPantalla()
        else:
            QtGui.QMessageBox.about(self, "Mensaje", "No le quedan mas ayudas :(")
            self.ui.cmdHint.setEnabled(False)
        
                    
    def calcularPuntaje(self):
        b=0
        for i in range(0,9):
            for j in range(0,9):
                try:
                    a = self.tableroActual[i][j]
                except AttributeError:
                    print "aun no ha empezado a jugar"
                    return 0 
                if a!=0:
                    b = b+1  
        if self.dificultad == 0:
            return (b-30)*10-self.tm.minute()
        if self.dificultad == 1:
            return (b-30)*10-self.tm.minute()
        if self.dificultad == 2:
            return (b-30)*10-self.tm.minute()
        if self.dificultad == 3:
            return (b-30)*10-self.tm.minute()
        return 0
            
  
    
                         
def main():
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
 
if __name__ == "__main__":
    main()