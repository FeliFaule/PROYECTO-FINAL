# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'recepcionista_turnos.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(748, 609)
        MainWindow.setMinimumSize(QtCore.QSize(748, 609))
        MainWindow.setMaximumSize(QtCore.QSize(748, 609))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 130, 71, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 91, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 260, 57, 15))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(300, 30, 211, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 310, 101, 20))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(90, 370, 141, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.botonguardar = QtWidgets.QPushButton(self.centralwidget)
        self.botonguardar.setGeometry(QtCore.QRect(560, 480, 161, 61))
        self.botonguardar.setObjectName("botonguardar")
        self.botosalir = QtWidgets.QPushButton(self.centralwidget)
        self.botosalir.setGeometry(QtCore.QRect(50, 480, 161, 61))
        self.botosalir.setObjectName("botosalir")
        self.editnombre = QtWidgets.QTextEdit(self.centralwidget)
        self.editnombre.setGeometry(QtCore.QRect(250, 120, 291, 41))
        self.editnombre.setObjectName("editnombre")
        self.editapellido = QtWidgets.QTextEdit(self.centralwidget)
        self.editapellido.setGeometry(QtCore.QRect(250, 180, 291, 41))
        self.editapellido.setObjectName("editapellido")
        self.editDNI = QtWidgets.QTextEdit(self.centralwidget)
        self.editDNI.setGeometry(QtCore.QRect(250, 240, 291, 41))
        self.editDNI.setObjectName("editDNI")
        self.edittelefono = QtWidgets.QTextEdit(self.centralwidget)
        self.edittelefono.setGeometry(QtCore.QRect(250, 300, 291, 41))
        self.edittelefono.setObjectName("edittelefono")
        self.editobrasocial = QtWidgets.QTextEdit(self.centralwidget)
        self.editobrasocial.setGeometry(QtCore.QRect(250, 360, 291, 41))
        self.editobrasocial.setObjectName("editobrasocial")
        self.Timeeditfecha = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.Timeeditfecha.setGeometry(QtCore.QRect(250, 420, 291, 41))
        self.Timeeditfecha.setObjectName("Timeeditfecha")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 430, 61, 16))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.botonguardar.clicked['bool'].connect(MainWindow.guardar) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NOMBRE"))
        self.label_2.setText(_translate("MainWindow", "APELLIDO"))
        self.label_3.setText(_translate("MainWindow", "DNI"))
        self.label_4.setText(_translate("MainWindow", "NUEVO TURNO"))
        self.label_5.setText(_translate("MainWindow", "TELEFONO"))
        self.label_6.setText(_translate("MainWindow", "OBRA SOCIAL"))
        self.botonguardar.setText(_translate("MainWindow", "GUARDAR"))
        self.botosalir.setText(_translate("MainWindow", "SALIR"))
        self.label_7.setText(_translate("MainWindow", "FECHA"))
