# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resetas.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 350)
        MainWindow.setMinimumSize(QtCore.QSize(450, 350))
        MainWindow.setMaximumSize(QtCore.QSize(450, 350))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(150, 10, 158, 42))
        self.title_label.setObjectName("title_label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 50, 601, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tipo_farmaco_label = QtWidgets.QLabel(self.centralwidget)
        self.tipo_farmaco_label.setGeometry(QtCore.QRect(50, 90, 102, 15))
        self.tipo_farmaco_label.setObjectName("tipo_farmaco_label")
        self.cantidad_famaco_label = QtWidgets.QLabel(self.centralwidget)
        self.cantidad_famaco_label.setGeometry(QtCore.QRect(50, 130, 134, 15))
        self.cantidad_famaco_label.setObjectName("cantidad_famaco_label")
        self.por_cuanto_label = QtWidgets.QLabel(self.centralwidget)
        self.por_cuanto_label.setGeometry(QtCore.QRect(50, 170, 114, 15))
        self.por_cuanto_label.setObjectName("por_cuanto_label")
        self.cada_cuanto_label = QtWidgets.QLabel(self.centralwidget)
        self.cada_cuanto_label.setGeometry(QtCore.QRect(50, 210, 126, 15))
        self.cada_cuanto_label.setObjectName("cada_cuanto_label")
        self.tipo_farmaco_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tipo_farmaco_lineEdit.setGeometry(QtCore.QRect(190, 90, 251, 23))
        self.tipo_farmaco_lineEdit.setObjectName("tipo_farmaco_lineEdit")
        self.cantidad_farmaco_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cantidad_farmaco_lineEdit.setGeometry(QtCore.QRect(190, 130, 251, 23))
        self.cantidad_farmaco_lineEdit.setObjectName("cantidad_farmaco_lineEdit")
        self.por_cuanto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.por_cuanto_lineEdit.setGeometry(QtCore.QRect(190, 170, 251, 23))
        self.por_cuanto_lineEdit.setObjectName("por_cuanto_lineEdit")
        self.cada_cuanto_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.cada_cuanto_lineEdit.setGeometry(QtCore.QRect(190, 210, 251, 23))
        self.cada_cuanto_lineEdit.setObjectName("cada_cuanto_lineEdit")
        self.crear_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.crear_pushButton.setGeometry(QtCore.QRect(170, 250, 86, 23))
        self.crear_pushButton.setObjectName("crear_pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 20))
        self.menubar.setObjectName("menubar")
        self.menuRECETAS = QtWidgets.QMenu(self.menubar)
        self.menuRECETAS.setObjectName("menuRECETAS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuRECETAS.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">RECETAS</span></p></body></html>"))
        self.tipo_farmaco_label.setText(_translate("MainWindow", "Tipo de farmaco:"))
        self.cantidad_famaco_label.setText(_translate("MainWindow", "Cantidad del farmaco:"))
        self.por_cuanto_label.setText(_translate("MainWindow", "Por cuanto tiempo:"))
        self.cada_cuanto_label.setText(_translate("MainWindow", "Cada cuanto tiempo:"))
        self.crear_pushButton.setText(_translate("MainWindow", "Crear Reseta"))
        self.menuRECETAS.setTitle(_translate("MainWindow", "RECETAS"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
