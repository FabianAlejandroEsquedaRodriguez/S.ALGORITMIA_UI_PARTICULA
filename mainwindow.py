from math import dist
from pprint import pformat
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform, qBlue, qRed, qRgb
from PySide2.QtCore import Slot
from random import randint
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

        #Crear la escena, despues de haber conectaro
        self.scene = QGraphicsScene()#Es como si fuera un visualizador de dibujos
        self.ui.graphicsView.setScene(self.scene)#En el graphicsView, se inserta la escena creada

        #conectar los botones a sus metodos
        self.ui.ordenar_id_pushButton.clicked.connect(self.ordenar_id)
        self.ui.ordenar_distancia_pushButton_2.clicked.connect(self.ordenar_distancia)
        self.ui.ordenar_velocidad_pushButton_3.clicked.connect(self.ordenar_velocidad)

        #Conectar los botones con sus metodos
        self.ui.mostrar_grafo_pushButton.clicked.connect(self.dibujar_grafo)

        #Conectar la señal para su metodo de recorrido en anchura/profundidad
        self.ui.actionAmplitud_Profundidad.triggered.connect(self.recorrido_amplitud_profundidad)

        #Conectar la señal para su metodo de recorrido con el algoritmo de Prim
        self.ui.actionPrim.triggered.connect(self.recorridoPrim)

        #Conectar la señal para su metodo de recorrido con Kruskal
        self.ui.actionKruskal.triggered.connect(self.recorridoKruskal)

        #Conectar la señal para su metodo de recorrido dijkstra
        self.ui.actionDijkstra.triggered.connect(self.recorridoDijkstra)
    

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

    def wheelEvent(self, event):#Detecta el evento de la ruedita del mouse para hacer zoom a la escena
        if event.delta() > 0:#Para hecer zoom in
            self.ui.graphicsView.scale(1.2, 1.2)#1.2 en x, y
        else:#Para hacer el zoom out
            self.ui.graphicsView.scale(0.8, 0.8)#0.8 en x, y

    @Slot()
    def dibujar(self):
        pen = QPen()#crear una pluma, que esta definida en la clase QPen
        pen.setWidth(3)#Tamaño/anchura de la pluma

        for particula in self.contenedor_particulas:
            #Ponerle color a la puma
            r = particula.red#randint(0, 255)#Generar un color de manera aleatoria
            g = particula.green#randint(0, 255)#entre 0 y 255
            b = particula.blue#randint(0, 255)

            color = QColor(r, g, b)

            pen.setColor(color)#Asignarle el color a la variable pluma

            #Posiciones de origen y destino 
            origen_x = particula.origen_x#randint(0, 500)
            origen_y = particula.origen_y#randint(0, 500)
            destino_x = particula.destino_x#randint(0, 500)
            destino_y = particula.destino_y#randint(0, 500)

            self.scene.addEllipse(origen_x, origen_y, 3, 3, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
            self.scene.addEllipse(destino_x, destino_y, 3, 3, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
            
            #Para dibujar una linea para conectar los 2 puntos
            self.scene.addLine(origen_x+2, origen_y+2,
                                destino_x, destino_y, pen)#Origen en 'x','y' y destino en 'x','y', 
                                                            #el +3 es para dibujar la linea un poco mas abajo 

    @Slot()
    def limpiar(self):
        self.scene.clear()

    @Slot()
    def ordenar_id(self):#Manda a llamar un metodo que se encuentra en la clase administradora
        self.contenedor_particulas.ordenar_ID()

    @Slot()
    def ordenar_distancia(self):#Manda a llamar un metodo que se encuentra en la clase administradora
        self.contenedor_particulas.ordenar_DISTANCIA()

    @Slot()
    def ordenar_velocidad(self):#Manda a llamar un metodo que se encuentra en la clase administradora
        self.contenedor_particulas.ordenar_VELOCIDAD()

    @Slot()
    def dibujar_grafo(self):
        self.ui.salida_grafo.clear()

        texto = self.contenedor_particulas.Diccionario()

        str = pformat(texto, width=40, indent=1)
        print(str)#Imprime el grafo en la terminal
        self.ui.salida_grafo.insertPlainText(str)
        
        self.dibujar()

    @Slot()
    def recorrido_amplitud_profundidad(self):
        self.ui.salida_grafo.clear()

        origen_x = self.ui.orig_x_spinBox.value()
        origen_y = self.ui.orig_y_spinBox.value()

        recorridoP = self.contenedor_particulas.recorridoP(origen_x, origen_y)
        self.ui.salida_grafo.insertPlainText("RECORRIDO EN PROFUNDIDAD\n\n")
        self.ui.salida_grafo.insertPlainText(recorridoP)

        recorridoA = self.contenedor_particulas.recorridoA(origen_x, origen_y)
        self.ui.salida_grafo.insertPlainText("\n\n\nRECORRIDO EN AMPLITUD\n\n")
        self.ui.salida_grafo.insertPlainText(recorridoA)

    @Slot()
    def recorridoPrim(self):
        pen = QPen()#crear una pluma, que esta definida en la clase QPen
        pen.setWidth(3)#Tamaño/anchura de la pluma

        self.ui.salida_grafo.clear()

        origen_x = self.ui.orig_x_spinBox.value()
        origen_y = self.ui.orig_y_spinBox.value()

        expansionMinPrim = self.contenedor_particulas.PRIM(origen_x, origen_y)
        str = pformat(expansionMinPrim, width=40, indent=1)

        self.ui.salida_grafo.insertPlainText("RECORRIDO -> ALGORITMO DE PRIM\n\n")
        self.ui.salida_grafo.insertPlainText(str)

        color = QColor(245, 0, 135)
        pen.setColor(color)#Asignarle el color a la variable pluma
        
        #Para dibujar el grafo
        key = (origen_x, origen_y)

        for key in expansionMinPrim.keys():
            orig_x = key[0]
            orig_y = key[1]
            # print('\n',orig_x, orig_y)

            for valor in expansionMinPrim[key]:
                destino = valor[0]
                destino_x = destino[0]
                destino_y = destino[1]
                # print(destino)

                self.scene.addEllipse(orig_x, orig_y, 4, 4, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
                self.scene.addEllipse(destino_x, destino_y, 4, 4, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
                
                # #Para dibujar una linea para conectar los 2 puntos
                self.scene.addLine(orig_x+2, orig_y+2,
                                    destino_x, destino_y, pen)#Origen en 'x','y' y destino en 'x','y', 
                                                        #el +3 es para dibujar la linea un poco mas abajo

    @Slot()
    def recorridoKruskal(self):
        self.ui.salida_grafo.clear()

        recorrido_kruskal = self.contenedor_particulas.recorridoKruskal()
        str = pformat(recorrido_kruskal, width=40, indent=1)

        self.ui.salida_grafo.insertPlainText("RECORRIDO -> ALGORITMO DE KRUSKAL\n\n")
        self.ui.salida_grafo.insertPlainText(str)

        pen = QPen()
        pen.setWidth(3)

        color = QColor(245, 0, 135)
        pen.setColor(color)

        for key in recorrido_kruskal.keys():
            orig_x = key[0]
            orig_y = key[1]

            for values in recorrido_kruskal[key]:
                destino = values[1]
                dest_x = destino[0]
                dest_y = destino[1]

                self.scene.addEllipse(orig_x, orig_y, 4, 4, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
                self.scene.addEllipse(dest_x, dest_y, 4, 4, pen)#En que posicion se va a dibujar (x,y) y el radio (3,3) y la pluma
                
                # #Para dibujar una linea para conectar los 2 puntos
                self.scene.addLine(orig_x+2, orig_y+2,
                                    dest_x, dest_y, pen)#Origen en 'x','y' y destino en 'x','y', 
                                                        #el +3 es para dibujar la linea un poco mas abajo

    @Slot()
    def recorridoDijkstra(self):
        self.ui.salida_grafo.clear()
        self.scene.clear()
        
        pen = QPen()
        pen.setWidth(3)

        color = QColor(245, 0, 135)
        pen.setColor(color)

        orig_x = self.ui.orig_x_spinBox.value()
        orig_y = self.ui.orig_y_spinBox.value()
        dest_x = self.ui.dest_x_spinBox.value()
        dest_y = self.ui.dest_y_spinBox.value()

        recorrido_Dijkstra = self.contenedor_particulas.recorridoDijkstra(orig_x, orig_y)

        str = pformat(recorrido_Dijkstra, width=40, indent=1)

        self.ui.salida_grafo.insertPlainText("RECORRIDO (CAMINO) -> ALGORITMO DE DIJKSTRA\n\n")
        self.ui.salida_grafo.insertPlainText(str)


        origenDIJ = (dest_x, dest_y)#El destino es a partir de donde va a iniciar a dibujar
        destinoDIJ = (orig_x, orig_y)#hasta llegar al origen

        ady = recorrido_Dijkstra.get(origenDIJ)

        or_x = origenDIJ[0]#Elorigen x, va a ser el destino x
        or_y = origenDIJ[1]#El origen y, va a ser el destino y

        dest_x = ady[0]
        dest_y = ady[1]

        self.scene.addEllipse(or_x, or_y, 4, 4, pen)
        self.scene.addEllipse(dest_x, dest_y, 4, 4, pen)
        self.scene.addLine(or_x+2, or_y+2, dest_x, dest_y, pen)

        while destinoDIJ != ady:
            nuevoDestino = (dest_x, dest_y)
            or_x = nuevoDestino[0]
            or_y = nuevoDestino[1]

            ady = recorrido_Dijkstra.get(nuevoDestino)


            dest_x = ady[0]
            dest_y = ady[1]

            self.scene.addEllipse(or_x, or_y, 4, 4, pen)
            self.scene.addEllipse(dest_x, dest_y, 4, 4, pen)
            self.scene.addLine(or_x+2, or_y+2, dest_x, dest_y, pen)