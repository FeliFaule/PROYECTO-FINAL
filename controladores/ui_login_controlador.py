import json
from interfaces.ui_login import Ui_LoginWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import pyqtSlot

# TODA LA LOGICA DE LA VENTANA LOGIN

class Login(QMainWindow, Ui_LoginWindow):
    def __init__(self):  # Constructor de la clase Login
        super().__init__()  # Llama al constructor de QMainWindow, inicializando la ventana
        self.setupUi(self)  # Llama a setupUi correctamente, pasándole la instancia de 'self' (Login)
        self.login_button.clicked.connect(self.login)  # Conectar el botón al slot 'login'    

    @pyqtSlot()
    def login(self):
        file_path = 'datos/usuarios.json'     
        user = self.user_data.text().upper()
        password = self.password_data.text().upper()

        try:
            usuario_verificado = False
            
            # Abrir el archivo csv en modo lectura
            with open(file_path, 'r') as archivo:
                contenido = json.load(archivo)
                usuarios = contenido["usuarios"]
                usuario_verificado = next((fila for fila in usuarios if fila["nombre"] == user and fila["contrasena"] == password), None)
                
                if usuario_verificado:
                    print(f"Encontrado: {usuario_verificado["nombre"]} con password: {usuario_verificado["contrasena"]} y Rol: {usuario_verificado["rol"]}")

                    # Si tiene el rol MEDICO, abre la pantalla de atención de pacientes
                    if usuario_verificado["rol"] == 'MEDICO':
                        QMessageBox.information(self, "OK", f"ABRIR PANTALLA DEL MEDICO",QMessageBox.StandardButton.Close)
                    
                    # Si tiene el rol RECEPCION, abre la pantalla de recepción de pacientes
                    elif usuario_verificado["rol"] == 'RECEPCIONISTA':
                        QMessageBox.information(self, "OK", f"ABRIR PANTALLA DEL RECEPCIONISTA",QMessageBox.StandardButton.Close)
                    
                    # Si el rol no existe, debe informar que el usuario no tiene especificado un ROL válido.
                    else:
                        QMessageBox.critical(self, "Error", f"El usuario {user} no tiene un ROL válido. Contacta al administrador",QMessageBox.StandardButton.Close)


                else:
                    QMessageBox.critical(self, "Error", "Usuario o contraseña incorrectos",QMessageBox.StandardButton.Retry,QMessageBox.StandardButton.Retry)


        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de usuarios no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de usuarios.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los usuarios: {e}")