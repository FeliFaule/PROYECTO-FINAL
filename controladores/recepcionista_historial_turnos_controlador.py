import json
from interfaces.recepcionista_historialturnos import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot

class SecretarioWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargar_pacientes()

    @pyqtSlot()
    def cargar_pacientes(self):
        try:
            with open("datos/pacientes.json", "r") as file:
                pacientes = json.load(file)

            # Limpiar la tabla antes de insertar nuevos datos
            self.tablahistorialT.setRowCount(0)  # Limpiar la tabla

            # Insertar los datos de los pacientes en la tabla
            for paciente in pacientes["pacientes"]:
                # Agregar una nueva fila en la tabla
                row_position = self.tablahistorialT.rowCount()
                self.tablahistorialT.insertRow(row_position)

                # Insertar los datos del paciente en las celdas correspondientes
                self.tablahistorialT.setItem(row_position, 0, QTableWidgetItem(paciente["nombre"]))
                self.tablahistorialT.setItem(row_position, 1, QTableWidgetItem(paciente["apellido"]))
                self.tablahistorialT.setItem(row_position, 2, QTableWidgetItem(paciente["dni"]))
                self.tablahistorialT.setItem(row_position, 3, QTableWidgetItem(paciente["telefono"]))
                self.tablahistorialT.setItem(row_position, 4, QTableWidgetItem(paciente["obra_social"]))
                self.tablahistorialT.setItem(row_position, 5, QTableWidgetItem(paciente["fecha_turno"]))
        
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

