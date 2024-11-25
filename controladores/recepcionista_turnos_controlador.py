from clases.class_turno import Turno
from interfaces.recepcionista_turnos import Ui_modalNuevoTurno
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from datetime import datetime

class VentanaNuevoTurno(QDialog, Ui_modalNuevoTurno):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close(self):
        return super().close()
    
    def guardarTurno(self):
        # Obtener los datos de los QLineEdit
        nombre = self.lineEdit_nombre.text()
        apellido = self.lineEdit_apellido.text()
        dni = self.lineEdit_dni.text()
        telefono = self.lineEdit_telefono.text()
        obra_social = self.lineEdit_obra_social.text()
        fecha_hora = datetime.now().strftime('%d-%m-%Y %H:%M')

        # Validar que el DNI sea un número y que no esté vacío
        try:
            is_number = int(dni)
        except ValueError:
            QtWidgets.QMessageBox.warning(self, 'Error', 'El DNI debe ser un número válido.')
            return

        # Crear el nuevo turno
        nuevo_turno = Turno()
        nuevo_turno.crearTurno(nombre, apellido, dni, telefono, obra_social, fecha_hora)
        
        # Se pregunta a la recepcionista si quiere registrar el turno
        respuesta = QtWidgets.QMessageBox.question(self, "Registrar Turno", "¿Deseas registrar el nuevo turno?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        # Procesar la respuesta del usuario
        if respuesta == QtWidgets.QMessageBox.Yes:
            turno_creado = nuevo_turno.registrarTurno()

        # Confirmar al usuario
        if turno_creado:
            QtWidgets.QMessageBox.information(self, 'Guardado', 'El turno ha sido guardado correctamente.')
        else:
            QtWidgets.QMessageBox.error(self, 'Error', 'El turno NO ha podido ser guardado debido a la ocurrencia de un error. Intente nuevamente.')

        # Limpiar los campos de entrada
        self.lineEdit_nombre.clear()
        self.lineEdit_apellido.clear()
        self.lineEdit_dni.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_obra_social.clear()
        self.lineEdit_nombre.setFocus()