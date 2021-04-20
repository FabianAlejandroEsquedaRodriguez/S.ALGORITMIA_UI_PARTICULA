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
        MainWindow.resize(627, 458)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.agregar_inicio_pushButton = QPushButton(self.centralwidget)
        self.agregar_inicio_pushButton.setObjectName(u"agregar_inicio_pushButton")

        self.gridLayout_2.addWidget(self.agregar_inicio_pushButton, 2, 0, 1, 1)

        self.mostrar_pushButton = QPushButton(self.centralwidget)
        self.mostrar_pushButton.setObjectName(u"mostrar_pushButton")

        self.gridLayout_2.addWidget(self.mostrar_pushButton, 3, 0, 1, 1)

        self.agregar_final_pushButton = QPushButton(self.centralwidget)
        self.agregar_final_pushButton.setObjectName(u"agregar_final_pushButton")
        self.agregar_final_pushButton.setEnabled(True)

        self.gridLayout_2.addWidget(self.agregar_final_pushButton, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
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

        self.salida = QPlainTextEdit(self.centralwidget)
        self.salida.setObjectName(u"salida")

        self.gridLayout_2.addWidget(self.salida, 0, 1, 4, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 627, 21))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.actionGuardar)

        self.retranslateUi(MainWindow)

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
        self.agregar_inicio_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Inicio", None))
        self.mostrar_pushButton.setText(QCoreApplication.translate("MainWindow", u"Mostrar", None))
        self.agregar_final_pushButton.setText(QCoreApplication.translate("MainWindow", u"Agregar Final", None))
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
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
    # retranslateUi

