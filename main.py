import sys
from PyQt5.QtWidgets import QApplication
from controladores.ui_login_controlador import Login



if __name__ == "__main__":
    app = QApplication(sys.argv)   
    mainwindow = Login() 
    mainwindow.show() 
    sys.exit(app.exec_())

