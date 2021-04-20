from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
from contenedor_particulas import Contenedor_particulas
from particula import Particula

class MainWindow(QMainWindow):#Clase Mainwindow que hereda desde QMainWindow
    def __init__(self):
        #Llama al constructor de QMainWindow(Le reserva memoria para poder crear una ventana)
        super(MainWindow, self).__init__()

        #Creando un objeto de tipo contenedor_particulas(), de forma global, usando self
        self.contenedor_particulas = Contenedor_particulas()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)#Mete los componentes de nuestra UI a una ventana vacio

        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar_final)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)
        
        #Conetar las señales con sus slots
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)


    @Slot()
    def click_agregar_final(self):
        id = self.ui.ID_lineEdit.text()
        origen_x = self.ui.OrigenX_spinBox.value()
        origen_y = self.ui.OrigenY_spinBox.value()
        destino_x = self.ui.DestinoX_spinBox.value()
        destino_y = self.ui.DestinoY_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.RED_spinBox.value()
        green = self.ui.GREEN_spinBox.value()
        blue = self.ui.BLUE_spinBox.value()
        #distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

        #Crear un objeto Particula y pasarle como parametro lo que se lleno en la UI, para despues agregarlo al contenedor
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.contenedor_particulas.agregar_final(particula)

    @Slot()
    def click_agregar_inicio(self):
        id = self.ui.ID_lineEdit.text()
        origen_x = self.ui.OrigenX_spinBox.value()
        origen_y = self.ui.OrigenY_spinBox.value()
        destino_x = self.ui.DestinoX_spinBox.value()
        destino_y = self.ui.DestinoY_spinBox.value()
        velocidad = self.ui.Velocidad_lineEdit.text()
        red = self.ui.RED_spinBox.value()
        green = self.ui.GREEN_spinBox.value()
        blue = self.ui.BLUE_spinBox.value()
        #distancia = distancia_euclidiana(origen_x, destino_x, origen_y, destino_y)

        #Crear un objeto Particula y pasarle como parametro lo que se lleno en la UI, para despues agregarlo al contenedor
        particula = Particula(id, origen_x, origen_y, destino_x, destino_y, velocidad, red, green, blue)
        self.contenedor_particulas.agregar_inicio(particula)

    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()#Limpiar la info. cada que se presiona el boton
        self.ui.salida.insertPlainText(str(self.contenedor_particulas))

    #Metodos a conectar con las acciones de Abrir y Guardar, en la interfaz
    @Slot()
    def action_abrir_archivo(self):
        print("abrir_archivo")

    @Slot()
    def action_guardar_archivo(self):
        # print("guardar_archivo")

        #El metodo regresa una ubicacion de donde esta el archivo
        ubicacion = QFileDialog.getSaveFileName(
            self,#Ese dialogo se va a mandar desde esta ventana
            'Guardar Archivo',#Titulo para la ventana de dialogo
            '.',#Desde que directorio se va a abrir el dialogo (con el punto, indica que se va a abrir desde donde se este 
                #corriendo el ejecutable, en este caso, desde la carpeta del proyecto, o lugar)
            'JSON (*.json)'#Extension que va a llevar el archivo
        )[0]#Que solo me regrese lo que hay en la posicion 0
        print(ubicacion)#imprime una tupla con 2 valores
                        #La primera posision [0] es la ubicacion, con el nombre del archivo y la extension
                        #la segunda posicion [1], nos va a decir que filtro se eligió (JSON)
        
        #Validar si fue posible guardar en esa posicion el archivo
        if self.contenedor_particulas.guardar(ubicacion):
            QMessageBox.information(
                self,#Desde donde se ejecuta esa ventana
                "Éxito",#Nombre de la ventana
                "Se pudo crear el archivo " + ubicacion#Mensaje en la ventana

            )
        #En caso de que no haya sido posible guardar el archivo
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo crear el archivo" + ubicacion
            )
