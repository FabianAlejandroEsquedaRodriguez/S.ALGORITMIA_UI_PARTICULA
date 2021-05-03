from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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

        #Conectar las señales a sus slots
        self.ui.mostrar_tabla_pushButton.clicked.connect(self.mostrar_tabla)
        self.ui.buscar_pushButton.clicked.connect(self.buscar_id)

        #Conectar las señales con sus slots
        self.ui.dibujar.clicked.connect(self.dibujar)
        self.ui.limpiar.clicked.connect(self.limpiar)



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
        # print("abrir_archivo")
        #obtener la informacion para crear el dialogo, para que el usuario elija el archivo que quiera abrir
        ubicacion = QFileDialog.getOpenFileName(
            self,#Desde donde se va a lanzar la ventana
            'Abrir Archivo',#El nombre de la ventana de dialogo
            '.',#Desde donde se va a abrir el dialogo para seleccionar el archivo
            'JSON (*.json)'#El filtro, para poder elegir los archivos que seand e tipo json
        )[0]#Nos regresa la ubcacion del archivo
        if self.contenedor_particulas.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Éxito",
                "Se abrió el archivo " + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "Error al abrir el archivo " + ubicacion
            )

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

    @Slot()
    def mostrar_tabla(self):
        #Configurar la tabla (10 columnas, 1 por atributo)
        self.ui.tabla.setColumnCount(10)
        #Definir los headers o encabezados
        headers = ["ID", "Origen X", "Origen Y", "Destino X", "Destino Y", 
                    "Velocidad", "Red", "Green", "Blue", "Distancia"]
        #Mandarle los headers a la tabla para que los agregue
        self.ui.tabla.setHorizontalHeaderLabels(headers)
        #Establecer filas (Corresponden a la cantidad de particulas capturadas)
        self.ui.tabla.setRowCount(len(self.contenedor_particulas))#Accede al metodo len() en la clase contenedor_particulas
        
        row = 0#contador de filas
        #Sacar cada particula del contenedor par ir construyendo cada fila
        for particula in self.contenedor_particulas:
           # print(particula)#La particula es imprimible gracias al __str__() de la clase particula

            #Cada atributo debe ser un Item, para poder meterlos a la tabla(construir los widgets)
            #convertirlos a strings porque son enteros
            id_widget = QTableWidgetItem(str(particula.id))
            origen_x_widget = QTableWidgetItem(str(particula.origen_x))
            origen_y_widget = QTableWidgetItem(str(particula.origen_y))
            destino_x_widget = QTableWidgetItem(str(particula.destino_x))
            destino_y_widget = QTableWidgetItem(str(particula.destino_y))
            velocidad_widget = QTableWidgetItem(str(particula.velocidad))
            red_widget = QTableWidgetItem(str(particula.red))
            green_widget = QTableWidgetItem(str(particula.green))
            blue_widget = QTableWidgetItem(str(particula.blue))
            distancia_widget = QTableWidgetItem(str(particula.distancia))

            #Meter los items en cada columna que le corresponde
            self.ui.tabla.setItem(row, 0, id_widget)
            self.ui.tabla.setItem(row, 1, origen_x_widget)
            self.ui.tabla.setItem(row, 2, origen_y_widget)
            self.ui.tabla.setItem(row, 3, destino_x_widget)
            self.ui.tabla.setItem(row, 4, destino_y_widget)
            self.ui.tabla.setItem(row, 5, velocidad_widget)
            self.ui.tabla.setItem(row, 6, red_widget)
            self.ui.tabla.setItem(row, 7, green_widget)
            self.ui.tabla.setItem(row, 8, blue_widget)
            self.ui.tabla.setItem(row, 9, distancia_widget)

            row += 1#para que vaya pasando a la siguiente fila

    @Slot()
    def buscar_id(self):
        # print("buscar")
        id = self.ui.buscar_lineEdit.text()#obtener la informacion introducida en el lineEdit
        encontrado = False#bandera

        for particula in self.contenedor_particulas:
            if id == particula.id:#Si el id introducido en el lineEdit es igual al de la particula
                #Limpiar la tabla, si se encuentra la particula 
                # (Si hay info. en la tabla, la limpia e inserta la encontrada)
                self.ui.tabla.clear()
                self.ui.tabla.setRowCount(1)#la tabla va a tener una sola fila

                #insertar la particula en la tabla
                #Cada atributo debe ser un Item, para poder meterlos a la tabla(construir los widgets)
                #convertirlos a strings porque son enteros
                id_widget = QTableWidgetItem(str(particula.id))
                origen_x_widget = QTableWidgetItem(str(particula.origen_x))
                origen_y_widget = QTableWidgetItem(str(particula.origen_y))
                destino_x_widget = QTableWidgetItem(str(particula.destino_x))
                destino_y_widget = QTableWidgetItem(str(particula.destino_y))
                velocidad_widget = QTableWidgetItem(str(particula.velocidad))
                red_widget = QTableWidgetItem(str(particula.red))
                green_widget = QTableWidgetItem(str(particula.green))
                blue_widget = QTableWidgetItem(str(particula.blue))
                distancia_widget = QTableWidgetItem(str(particula.distancia))

                #Meter los items en cada columna que le corresponde
                self.ui.tabla.setItem(0, 0, id_widget)
                self.ui.tabla.setItem(0, 1, origen_x_widget)
                self.ui.tabla.setItem(0, 2, origen_y_widget)
                self.ui.tabla.setItem(0, 3, destino_x_widget)
                self.ui.tabla.setItem(0, 4, destino_y_widget)
                self.ui.tabla.setItem(0, 5, velocidad_widget)
                self.ui.tabla.setItem(0, 6, red_widget)
                self.ui.tabla.setItem(0, 7, green_widget)
                self.ui.tabla.setItem(0, 8, blue_widget)
                self.ui.tabla.setItem(0, 9, distancia_widget)

                #Si encontro la particula
                encontrado = True

                return#Para que no siga buscando

        if not encontrado:
            QMessageBox.warning(
                self,
                "Atención",#Nombre de la advertencia
                f'La particula con el ID "{id}", no fue encontrado'#f -> formato y "{variable}", podemos poner variables
                                                                #externas en los strings
            )

    @Slot()
    def dibujar(self):
        print("Dibujar")

    @Slot()
    def limpiar(self):
        print("limpiar")