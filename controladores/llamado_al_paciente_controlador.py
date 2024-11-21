import json
import serial
import time
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from interfaces.llamado_al_paciente import Ui_MainWindow
from controladores.todos_los_pacientes_controlador import verPacientes


class AtencionPacienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargarTurnos()


    def cargarTurnos(self):    
        try:
            with open("datos/turnos.json", "r") as file:
                turnos = json.load(file)
                #contenido = json.load(file)
                #pacientes = contenido["pacientes"]

            # Limpiar la tabla antes de insertar nuevos datos
            self.listado_turnos.setRowCount(0)  # Limpiar la tabla

            # Insertar los datos de los pacientes en la tabla
            for turno in turnos["turno"]:
                # Agregar una nueva fila en la tabla
                row_position = self.listado_turnos.rowCount()
                self.listado_turnos.insertRow(row_position)

                # Insertar los datos del paciente en las celdas correspondientes
                self.listado_turnos.setItem(row_position, 0, QTableWidgetItem(turno["nombre"]))
                self.listado_turnos.setItem(row_position, 1, QTableWidgetItem(turno["apellido"]))
                self.listado_turnos.setItem(row_position, 2, QTableWidgetItem(turno["dni"]))
                self.listado_turnos.setItem(row_position, 3, QTableWidgetItem(turno["telefono"]))
                self.listado_turnos.setItem(row_position, 4, QTableWidgetItem(turno["obra_social"]))
                self.listado_turnos.setItem(row_position, 5, QTableWidgetItem(turno["fecha_hora"]))

            self.listado_turnos.resizeColumnsToContents()
        
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

    def llamar_paciente(self):
        # Aquí puedes definir la acción para llamar a un paciente.
        # Por ejemplo, obtener el nombre del paciente de la primera fila seleccionada.
        row = self.listado_turnos.currentRow()
        if row >= 0:
            nombre_paciente = self.listado_turnos.item(row, 0).text()
            QMessageBox.information(self, "Llamar Paciente", f"Llamando a: {nombre_paciente}")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para llamar.")

    def atender_paciente(self):
        # Aquí puedes definir la acción para atender al paciente.
        # Por ejemplo, obtener el nombre del paciente de la primera fila seleccionada.
        row = self.listado_turnos.currentRow()
        if row >= 0:
            nombre_paciente = self.listado_turnos.item(row, 0).text()
            QMessageBox.information(self, "Atender Paciente", f"Atendiendo a: {nombre_paciente}")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para atender.")



    def abrirInfoPacientes(self):
        ventanaTurno = verPacientes()
        ventanaTurno.exec_()
        self.cargarTurnos()


    
