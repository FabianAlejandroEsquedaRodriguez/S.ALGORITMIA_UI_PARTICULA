# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'particula.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 471)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.actionAnchura_Profundidad = QAction(MainWindow)
        self.actionAnchura_Profundidad.setObjectName(u"actionAnchura_Profundidad")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_2 = QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BLUE_spinBox = QSpinBox(self.groupBox)
        self.BLUE_spinBox.setObjectName(u"BLUE_spinBox")
        self.BLUE_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.BLUE_spinBox, 9, 2, 1, 1)

        self.DestinoX_spinBox = QSpinBox(self.groupBox)
        self.DestinoX_spinBox.setObjectName(u"DestinoX_spinBox")
        self.DestinoX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoX_spinBox, 3, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.OrigenY_spinBox = QSpinBox(self.groupBox)
        self.OrigenY_spinBox.setObjectName(u"OrigenY_spinBox")
        self.OrigenY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenY_spinBox, 2, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.GREEN_spinBox = QSpinBox(self.groupBox)
        self.GREEN_spinBox.setObjectName(u"GREEN_spinBox")
        self.GREEN_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.GREEN_spinBox, 8, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.Velocidad_lineEdit = QLineEdit(self.groupBox)
        self.Velocidad_lineEdit.setObjectName(u"Velocidad_lineEdit")

        self.gridLayout.addWidget(self.Velocidad_lineEdit, 5, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.OrigenX_spinBox = QSpinBox(self.groupBox)
        self.OrigenX_spinBox.setObjectName(u"OrigenX_spinBox")
        self.OrigenX_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.OrigenX_spinBox, 1, 2, 1, 1)

        self.RED_spinBox = QSpinBox(self.groupBox)
        self.RED_spinBox.setObjectName(u"RED_spinBox")
        self.RED_spinBox.setMaximum(255)

        self.gridLayout.addWidget(self.RED_spinBox, 7, 2, 1, 1)

        self.DestinoY_spinBox = QSpinBox(self.groupBox)
        self.DestinoY_spinBox.setObjectName(u"DestinoY_spinBox")
        self.DestinoY_spinBox.setMaximum(500)

        self.gridLayout.addWidget(self.DestinoY_spinBox, 4, 2, 1, 1)

        self.ID_lineEdit = QLineEdit(self.groupBox)
        self.ID_lineEdit.setObjectName(u"ID_lineEdit")

        self.gridLayout.addWidget(self.ID_lineEdit, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.tab)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setEnabled(True)

        self.gridLayout_2.addWidget(self.agregar_final_pushButton, 1, 0, 1, 1)

        self.agregar_inicio_pushButton = QPushButton(self.tab)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 2, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.tab)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 3, 0, 1, 1)

        self.salida = QPlainTextEdit(self.tab)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 4, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabla = QTableWidget(self.tab_2)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout_4.addWidget(self.tabla, 0, 0, 1, 3)

        self.buscar_lineEdit = QLineEdit(self.tab_2)
        self.buscar_lineEdit.setObjectName(u"buscar_lineEdit")

        self.gridLayout_4.addWidget(self.buscar_lineEdit, 1, 0, 1, 1)

        self.buscar_pushButton = QPushButton(self.tab_2)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")

        self.gridLayout_4.addWidget(self.buscar_pushButton, 1, 1, 1, 1)

        self.mostrar_tabla_pushButton = QPushButton(self.tab_2)
        self.mostrar_tabla_pushButton.setObjectName(u"mostrar_tabla_pushButton")

        self.gridLayout_4.addWidget(self.mostrar_tabla_pushButton, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.ordenar_distancia_pushButton_2 = QPushButton(self.tab_4)
        self.ordenar_distancia_pushButton_2.setObjectName(u"ordenar_distancia_pushButton_2")
        self.ordenar_distancia_pushButton_2.setGeometry(QRect(310, 20, 281, 171))
        self.ordenar_id_pushButton = QPushButton(self.tab_4)
        self.ordenar_id_pushButton.setObjectName(u"ordenar_id_pushButton")
        self.ordenar_id_pushButton.setGeometry(QRect(10, 20, 281, 171))
        self.ordenar_velocidad_pushButton_3 = QPushButton(self.tab_4)
        self.ordenar_velocidad_pushButton_3.setObjectName(u"ordenar_velocidad_pushButton_3")
        self.ordenar_velocidad_pushButton_3.setGeometry(QRect(9, 218, 581, 161))
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.graphicsView = QGraphicsView(self.tab_3)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(195, 30, 401, 321))
        self.dibujar = QPushButton(self.tab_3)
        self.dibujar.setObjectName(u"dibujar")
        self.dibujar.setGeometry(QRect(200, 360, 131, 23))
        self.limpiar = QPushButton(self.tab_3)
        self.limpiar.setObjectName(u"limpiar")
        self.limpiar.setGeometry(QRect(470, 360, 121, 23))
        self.mostrar_grafo_pushButton = QPushButton(self.tab_3)
        self.mostrar_grafo_pushButton.setObjectName(u"mostrar_grafo_pushButton")
        self.mostrar_grafo_pushButton.setGeometry(QRect(340, 360, 121, 23))
        self.label_11 = QLabel(self.tab_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 10, 121, 16))
        self.salida_grafo = QPlainTextEdit(self.tab_3)
        self.salida_grafo.setObjectName(u"salida_grafo")
        self.salida_grafo.setGeometry(QRect(10, 30, 171, 281))
        self.label_12 = QLabel(self.tab_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 320, 61, 16))
        self.label_13 = QLabel(self.tab_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(20, 350, 61, 16))
        self.orig_x_spinBox = QSpinBox(self.tab_3)
        self.orig_x_spinBox.setObjectName(u"orig_x_spinBox")
        self.orig_x_spinBox.setGeometry(QRect(80, 320, 101, 22))
        self.orig_x_spinBox.setMaximum(500)
        self.orig_y_spinBox = QSpinBox(self.tab_3)
        self.orig_y_spinBox.setObjectName(u"orig_y_spinBox")
        self.orig_y_spinBox.setGeometry(QRect(80, 350, 101, 22))
        self.orig_y_spinBox.setMaximum(500)
        self.tabWidget.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuRecorridos = QMenu(self.menubar)
        self.menuRecorridos.setObjectName(u"menuRecorridos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuRecorridos.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuRecorridos.addAction(self.actionAnchura_Profundidad)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(shortcut)
        self.actionAbrir.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
#if QT_CONFIG(shortcut)
        self.actionGuardar.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionAnchura_Profundidad.setText(QCoreApplication.translate("MainWindow", u"Busqueda en Anchura/Profundidad", None))
#if QT_CONFIG(shortcut)
        self.actionAnchura_Profundidad.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"PARTICULA", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ORIGEN EN Y: ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"COLOR:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"DESTINO X:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"- BLUE: ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"- GREEN:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ORIGEN EN X:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"- RED:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"DESTINO Y:", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.buscar_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID de la Particula", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.mostrar_tabla_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tabla", None))
        self.ordenar_distancia_pushButton_2.setText(QCoreApplication.translate("MainWindow", u"DISTANCIA (DESCENDENTE)", None))
        self.ordenar_id_pushButton.setText(QCoreApplication.translate("MainWindow", u"ID (ASENDENTE)", None))
        self.ordenar_velocidad_pushButton_3.setText(QCoreApplication.translate("MainWindow", u"VELOCIDAD (ASCENDENTE)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Ordenar", None))
        self.dibujar.setText(QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.mostrar_grafo_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar Grafo", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Salida para el grafo:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ORIGEN X:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ORIGEN Y:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Dibujar", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuRecorridos.setTitle(QCoreApplication.translate("MainWindow", u"Recorridos", None))
    # retranslateUi

