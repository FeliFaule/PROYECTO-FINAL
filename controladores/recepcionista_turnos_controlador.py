from interfaces.recepcionista_turnos import Ui_modalNuevoTurno
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
import json
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
        nuevo_turno = {
            "nombre": nombre,
            "apellido": apellido,
            "dni": dni,
            "telefono": telefono,
            "obra_social": obra_social,
            "fecha_hora": fecha_hora
        }
        
        # Leer el archivo JSON y agregar el nuevo turno
        try:
            with open('datos/turnos.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"turno": []}  # Si el archivo no existe, creamos la estructura inicial

        # Agregar el nuevo turno a la lista de turnos
        data["turno"].append(nuevo_turno)

        # Guardar los datos actualizados en el archivo JSON
        with open('datos/turnos.json', 'w') as file:
            json.dump(data, file, indent=4)
        
        # Confirmar al usuario
        QtWidgets.QMessageBox.information(self, 'Guardado', 'El turno ha sido guardado correctamente.')

        # Limpiar los campos de entrada
        self.lineEdit_nombre.clear()
        self.lineEdit_apellido.clear()
        self.lineEdit_dni.clear()
        self.lineEdit_telefono.clear()
        self.lineEdit_obra_social.clear()
        self.lineEdit_nombre.setFocus()