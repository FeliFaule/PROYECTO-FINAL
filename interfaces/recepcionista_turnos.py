# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../diseños_qt/recepcionista_turnos.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modalNuevoTurno(object):
    def setupUi(self, modalNuevoTurno):
        modalNuevoTurno.setObjectName("modalNuevoTurno")
        modalNuevoTurno.resize(710, 420)
        modalNuevoTurno.setMinimumSize(QtCore.QSize(710, 420))
        modalNuevoTurno.setMaximumSize(QtCore.QSize(710, 420))
        self.widget = QtWidgets.QWidget(modalNuevoTurno)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 711, 461))
        self.widget.setObjectName("widget")
        self.label_imagen = QtWidgets.QLabel(self.widget)
        self.label_imagen.setGeometry(QtCore.QRect(-4, 0, 721, 461))
        self.label_imagen.setText("")
        self.label_imagen.setPixmap(QtGui.QPixmap("IMAGENES/Antecedentes médicos limpios _ Vector Gratis.jpg"))
        self.label_imagen.setScaledContents(True)
        self.label_imagen.setObjectName("label_imagen")
        self.label_name = QtWidgets.QLabel(self.widget)
        self.label_name.setGeometry(QtCore.QRect(104, 96, 47, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.botosalir = QtWidgets.QPushButton(self.widget)
        self.botosalir.setGeometry(QtCore.QRect(55, 342, 121, 30))
        self.botosalir.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.botosalir.setObjectName("botosalir")
        self.label_title = QtWidgets.QLabel(self.widget)
        self.label_title.setGeometry(QtCore.QRect(247, 30, 179, 33))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.botonguardar = QtWidgets.QPushButton(self.widget)
        self.botonguardar.setGeometry(QtCore.QRect(535, 342, 121, 30))
        self.botonguardar.setStyleSheet("QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    border-radius: 5px;\n"
"    padding: 5px 10px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"")
        self.botonguardar.setObjectName("botonguardar")
        self.label_lastname = QtWidgets.QLabel(self.widget)
        self.label_lastname.setGeometry(QtCore.QRect(104, 140, 63, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_lastname.setFont(font)
        self.label_lastname.setObjectName("label_lastname")
        self.label_obra_social = QtWidgets.QLabel(self.widget)
        self.label_obra_social.setGeometry(QtCore.QRect(103, 273, 86, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_obra_social.setFont(font)
        self.label_obra_social.setObjectName("label_obra_social")
        self.label_phone = QtWidgets.QLabel(self.widget)
        self.label_phone.setGeometry(QtCore.QRect(104, 229, 63, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_phone.setFont(font)
        self.label_phone.setObjectName("label_phone")
        self.label_dni = QtWidgets.QLabel(self.widget)
        self.label_dni.setGeometry(QtCore.QRect(104, 183, 24, 17))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_dni.setFont(font)
        self.label_dni.setObjectName("label_dni")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(196, 90, 421, 31))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_nombre.setFocus()
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(196, 133, 421, 31))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.lineEdit_dni = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_dni.setGeometry(QtCore.QRect(197, 176, 230, 31))
        self.lineEdit_dni.setObjectName("lineEdit_dni")
        self.lineEdit_telefono = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_telefono.setGeometry(QtCore.QRect(197, 220, 230, 31))
        self.lineEdit_telefono.setObjectName("lineEdit_telefono")
        self.lineEdit_obra_social = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_obra_social.setGeometry(QtCore.QRect(198, 264, 421, 31))
        self.lineEdit_obra_social.setObjectName("lineEdit_obra_social")

        self.retranslateUi(modalNuevoTurno)
        self.botosalir.clicked.connect(modalNuevoTurno.close) # type: ignore
        self.botonguardar.clicked.connect(modalNuevoTurno.guardarTurno) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(modalNuevoTurno)
        modalNuevoTurno.setTabOrder(self.lineEdit_nombre, self.lineEdit_apellido)
        modalNuevoTurno.setTabOrder(self.lineEdit_apellido, self.lineEdit_dni)
        modalNuevoTurno.setTabOrder(self.lineEdit_dni, self.lineEdit_telefono)
        modalNuevoTurno.setTabOrder(self.lineEdit_telefono, self.lineEdit_obra_social)
        modalNuevoTurno.setTabOrder(self.lineEdit_obra_social, self.botonguardar)
        modalNuevoTurno.setTabOrder(self.botonguardar, self.botosalir)

    def retranslateUi(self, modalNuevoTurno):
        _translate = QtCore.QCoreApplication.translate
        modalNuevoTurno.setWindowTitle(_translate("modalNuevoTurno", "NUEVO TURNO"))
        self.label_name.setText(_translate("modalNuevoTurno", "NOMBRE"))
        self.botosalir.setText(_translate("modalNuevoTurno", "SALIR"))
        self.label_title.setText(_translate("modalNuevoTurno", "NUEVO TURNO"))
        self.botonguardar.setText(_translate("modalNuevoTurno", "GUARDAR"))
        self.label_lastname.setText(_translate("modalNuevoTurno", "APELLIDO"))
        self.label_obra_social.setText(_translate("modalNuevoTurno", "OBRA SOCIAL"))
        self.label_phone.setText(_translate("modalNuevoTurno", "TELEFONO"))
        self.label_dni.setText(_translate("modalNuevoTurno", "DNI"))
