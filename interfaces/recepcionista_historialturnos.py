# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recepcionista_historialturnos.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecepcionistaMainWindow(object):
    def setupUi(self, RecepcionistaMainWindow):
        RecepcionistaMainWindow.setObjectName("RecepcionistaMainWindow")
        RecepcionistaMainWindow.setEnabled(True)
        RecepcionistaMainWindow.resize(705, 457)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecepcionistaMainWindow.sizePolicy().hasHeightForWidth())
        RecepcionistaMainWindow.setSizePolicy(sizePolicy)
        RecepcionistaMainWindow.setMinimumSize(QtCore.QSize(705, 457))
        RecepcionistaMainWindow.setMaximumSize(QtCore.QSize(705, 457))
        RecepcionistaMainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        RecepcionistaMainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(RecepcionistaMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 441))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../IMAGENES/Antecedentes médicos limpios _ Vector Gratis.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.titulo = QtWidgets.QLabel(self.widget)
        self.titulo.setGeometry(QtCore.QRect(300, 20, 100, 34))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.boton_nuevo_turno = QtWidgets.QPushButton(self.widget)
        self.boton_nuevo_turno.setGeometry(QtCore.QRect(240, 270, 101, 31))
        self.boton_nuevo_turno.setObjectName("boton_nuevo_turno")
        self.boton_salir = QtWidgets.QPushButton(self.widget)
        self.boton_salir.setGeometry(QtCore.QRect(360, 270, 101, 31))
        self.boton_salir.setObjectName("boton_salir")
        self.tablaListaTurnos = QtWidgets.QTableWidget(self.widget)
        self.tablaListaTurnos.setGeometry(QtCore.QRect(50, 70, 601, 192))
        self.tablaListaTurnos.setObjectName("tablaListaTurnos")
        self.tablaListaTurnos.setColumnCount(6)
        self.tablaListaTurnos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListaTurnos.setHorizontalHeaderItem(5, item)
        RecepcionistaMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RecepcionistaMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 20))
        self.menubar.setObjectName("menubar")
        RecepcionistaMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RecepcionistaMainWindow)
        self.statusbar.setObjectName("statusbar")
        RecepcionistaMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RecepcionistaMainWindow)
        self.boton_nuevo_turno.clicked.connect(RecepcionistaMainWindow.nuevoTurno) # type: ignore
        self.boton_salir.clicked.connect(RecepcionistaMainWindow.salir) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RecepcionistaMainWindow)

    def retranslateUi(self, RecepcionistaMainWindow):
        _translate = QtCore.QCoreApplication.translate
        RecepcionistaMainWindow.setWindowTitle(_translate("RecepcionistaMainWindow", "MainWindow"))
        self.titulo.setText(_translate("RecepcionistaMainWindow", "TURNOS"))
        self.boton_nuevo_turno.setText(_translate("RecepcionistaMainWindow", "NUEVO TURNO"))
        self.boton_salir.setText(_translate("RecepcionistaMainWindow", "SALIR"))
        item = self.tablaListaTurnos.horizontalHeaderItem(0)
        item.setText(_translate("RecepcionistaMainWindow", "APELLIDO"))
        item = self.tablaListaTurnos.horizontalHeaderItem(1)
        item.setText(_translate("RecepcionistaMainWindow", "NOMBRE"))
        item = self.tablaListaTurnos.horizontalHeaderItem(2)
        item.setText(_translate("RecepcionistaMainWindow", "DNI"))
        item = self.tablaListaTurnos.horizontalHeaderItem(3)
        item.setText(_translate("RecepcionistaMainWindow", "TELEFONO"))
        item = self.tablaListaTurnos.horizontalHeaderItem(4)
        item.setText(_translate("RecepcionistaMainWindow", "OBRA SOCIAL"))
        item = self.tablaListaTurnos.horizontalHeaderItem(5)
        item.setText(_translate("RecepcionistaMainWindow", "FECHA Y HORA"))
