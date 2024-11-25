# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../diseños_qt/recepcionista_historialturnos.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RecepcionistaMainWindow(object):
    def setupUi(self, RecepcionistaMainWindow):
        RecepcionistaMainWindow.setObjectName("RecepcionistaMainWindow")
        RecepcionistaMainWindow.setEnabled(True)
        RecepcionistaMainWindow.resize(1073, 666)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RecepcionistaMainWindow.sizePolicy().hasHeightForWidth())
        RecepcionistaMainWindow.setSizePolicy(sizePolicy)
        RecepcionistaMainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        RecepcionistaMainWindow.setDocumentMode(True)
        self.centralwidget = QtWidgets.QWidget(RecepcionistaMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1071, 661))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1071, 661))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("IMAGENES/background_image.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.titulo = QtWidgets.QLabel(self.widget)
        self.titulo.setGeometry(QtCore.QRect(480, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.boton_nuevo_turno = QtWidgets.QPushButton(self.widget)
        self.boton_nuevo_turno.setGeometry(QtCore.QRect(370, 610, 131, 31))
        self.boton_nuevo_turno.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.boton_nuevo_turno.setObjectName("boton_nuevo_turno")
        self.boton_salir = QtWidgets.QPushButton(self.widget)
        self.boton_salir.setGeometry(QtCore.QRect(570, 610, 131, 31))
        self.boton_salir.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}")
        self.boton_salir.setObjectName("boton_salir")
        self.tablaListaTurnos = QtWidgets.QTableWidget(self.widget)
        self.tablaListaTurnos.setGeometry(QtCore.QRect(10, 80, 1051, 511))
        self.tablaListaTurnos.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tablaListaTurnos.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablaListaTurnos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
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
        self.tablaListaTurnos.horizontalHeader().setDefaultSectionSize(175)
        self.tablaListaTurnos.horizontalHeader().setStretchLastSection(True)
        self.tablaListaTurnos.verticalHeader().setSortIndicatorShown(False)
        self.boton_ordenar = QtWidgets.QPushButton(self.widget)
        self.boton_ordenar.setGeometry(QtCore.QRect(950, 50, 111, 21))
        self.boton_ordenar.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.boton_ordenar.setObjectName("boton_ordenar")
        self.label.raise_()
        self.titulo.raise_()
        self.boton_nuevo_turno.raise_()
        self.boton_salir.raise_()
        self.boton_ordenar.raise_()
        self.tablaListaTurnos.raise_()
        RecepcionistaMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RecepcionistaMainWindow)
        self.boton_nuevo_turno.clicked.connect(RecepcionistaMainWindow.nuevoTurno) # type: ignore
        self.boton_salir.clicked.connect(RecepcionistaMainWindow.salir) # type: ignore
        self.boton_ordenar.clicked.connect(RecepcionistaMainWindow.ordenarTurnos) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(RecepcionistaMainWindow)

    def retranslateUi(self, RecepcionistaMainWindow):
        _translate = QtCore.QCoreApplication.translate
        RecepcionistaMainWindow.setWindowTitle(_translate("RecepcionistaMainWindow", "LISTADO DE TURNOS"))
        self.titulo.setText(_translate("RecepcionistaMainWindow", "TURNOS"))
        self.boton_nuevo_turno.setText(_translate("RecepcionistaMainWindow", "NUEVO TURNO"))
        self.boton_salir.setText(_translate("RecepcionistaMainWindow", "SALIR"))
        self.tablaListaTurnos.setSortingEnabled(False)
        item = self.tablaListaTurnos.horizontalHeaderItem(0)
        item.setText(_translate("RecepcionistaMainWindow", "NOMBRE"))
        item = self.tablaListaTurnos.horizontalHeaderItem(1)
        item.setText(_translate("RecepcionistaMainWindow", "APELLIDO"))
        item = self.tablaListaTurnos.horizontalHeaderItem(2)
        item.setText(_translate("RecepcionistaMainWindow", "DNI"))
        item = self.tablaListaTurnos.horizontalHeaderItem(3)
        item.setText(_translate("RecepcionistaMainWindow", "TELEFONO"))
        item = self.tablaListaTurnos.horizontalHeaderItem(4)
        item.setText(_translate("RecepcionistaMainWindow", "OBRA SOCIAL"))
        item = self.tablaListaTurnos.horizontalHeaderItem(5)
        item.setText(_translate("RecepcionistaMainWindow", "FECHA Y HORA"))
        self.boton_ordenar.setText(_translate("RecepcionistaMainWindow", "ORDENAR"))
