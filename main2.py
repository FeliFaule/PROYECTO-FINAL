import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from  controladores.recepcionista_historialturnos_controlador import Login


if __name__ == "__main__":
    app = QApplication(sys.argv)   
    window = Login() 
    window.show() 
    sys.exit(app.exec_()) 
