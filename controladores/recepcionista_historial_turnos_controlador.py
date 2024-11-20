import json
from interfaces.recepcionista_historialturnos import Ui_RecepcionistaMainWindow
from controladores.recepcionista_turnos_controlador import VentanaNuevoTurno
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox

class RecepcionistaWindow(QMainWindow, Ui_RecepcionistaMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargar_pacientes()

    
    def cargar_pacientes(self):
        try:
            with open("datos/pacientes.json", "r") as archivo:
                contenido = json.load(archivo)
                pacientes = contenido["pacientes"]

            # Limpiar la tabla antes de insertar nuevos datos
            self.tablaListaTurnos.setRowCount(0)  # Limpiar la tabla

            # Insertar los datos de los pacientes en la tabla
            for paciente in pacientes:
                # Agregar una nueva fila en la tabla
                row_position = self.tablaListaTurnos.rowCount()
                self.tablaListaTurnos.insertRow(row_position)

                # Insertar los datos del paciente en las celdas correspondientes
                self.tablaListaTurnos.setItem(row_position, 0, QTableWidgetItem(paciente["nombre"]))
                self.tablaListaTurnos.setItem(row_position, 1, QTableWidgetItem(paciente["apellido"]))
                self.tablaListaTurnos.setItem(row_position, 2, QTableWidgetItem(paciente["dni"]))
                self.tablaListaTurnos.setItem(row_position, 3, QTableWidgetItem(paciente["telefono"]))
                self.tablaListaTurnos.setItem(row_position, 4, QTableWidgetItem(paciente["obra_social"]))
                self.tablaListaTurnos.setItem(row_position, 5, QTableWidgetItem(paciente["fecha_hora"]))
            
            self.tablaListaTurnos.resizeColumnsToContents()
            
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

    def salir(self):
        return super().close()
    
    def nuevoTurno(self):
        ventanaTurno = VentanaNuevoTurno()
        ventanaTurno.exec_()
        self.cargar_pacientes()