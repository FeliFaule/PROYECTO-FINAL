

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(416, 250)
        LoginWindow.setMinimumSize(QtCore.QSize(416, 250))
        LoginWindow.setMaximumSize(QtCore.QSize(416, 250))
        LoginWindow.setIconSize(QtCore.QSize(24, 24))

        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 10, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(50, 100, 81, 20))
        self.user_label.setObjectName("user_label")

        self.user_data = QtWidgets.QLineEdit(self.centralwidget)
        self.user_data.setGeometry(QtCore.QRect(130, 100, 201, 23))
        self.user_data.setObjectName("user_data")

        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(50, 130, 81, 20))
        self.password_label.setObjectName("password_label")

        self.password_data = QtWidgets.QLineEdit(self.centralwidget)
        self.password_data.setGeometry(QtCore.QRect(130, 130, 201, 23))
        self.password_data.setObjectName("password_data")
        
        self.login_button = QtWidgets.QPushButton(self.centralwidget)
        self.login_button.setGeometry(QtCore.QRect(210, 160, 121, 31))
        self.login_button.setObjectName("login_button")

        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 20))
        self.menubar.setObjectName("menubar")
        self.menuLOGIN = QtWidgets.QMenu(self.menubar)
        self.menuLOGIN.setObjectName("menuLOGIN")
        LoginWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuLOGIN.menuAction())

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
        self.login_button.setText(_translate("LoginWindow", "Iniciar Sesion"))
        self.user_label.setText(_translate("LoginWindow", "Usuario:"))
        self.password_label.setText(_translate("LoginWindow", "Contraseña:"))
        self.title.setText(_translate("LoginWindow", "IDENTIFICACION"))
        self.menuLOGIN.setTitle(_translate("LoginWindow", "LOGIN"))
