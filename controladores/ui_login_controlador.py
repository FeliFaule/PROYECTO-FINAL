
from interfaces.ui_login import Ui_LoginWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot

# TODA LA LOGICA DE LA VENTA LOGIN

class Login(QMainWindow, Ui_LoginWindow):
    def __init__(self): #constructor method. Se ejuecuta cuando la instancia de la clase es creada.
        super().__init__() #llama al constructor de la clase QMainWindow, para inicializar las funcionalidades básicas de la ventana principal de la app.
        self.setupUi(self) 



        
    