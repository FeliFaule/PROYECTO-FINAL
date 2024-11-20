import json
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import pyqtSlot
from interfaces.llamado_al_paciente import Ui_MainWindow

class AtencionPacienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargar_turnos()

    @pyqtSlot()
    def cargar_turnos(self):
        try:
            with open("datos/pacientes.json", "r") as file:
                pacientes = json.load(file)

            # Limpiar la tabla antes de insertar nuevos datos
            self.listado_turnos.setRowCount(0)  # Limpiar la tabla

            # Insertar los datos de los pacientes en la tabla
            for paciente in pacientes["pacientes"]:
                # Agregar una nueva fila en la tabla
                row_position = self.listado_turnos.rowCount()
                self.listado_turnos.insertRow(row_position)

                # Insertar los datos del paciente en las celdas correspondientes
                self.listado_turnos.setItem(row_position, 0, QTableWidgetItem(paciente["nombre"]))
                self.listado_turnos.setItem(row_position, 1, QTableWidgetItem(paciente["apellido"]))
                self.listado_turnos.setItem(row_position, 2, QTableWidgetItem(paciente["dni"]))
                self.listado_turnos.setItem(row_position, 3, QTableWidgetItem(paciente["telefono"]))
                self.listado_turnos.setItem(row_position, 4, QTableWidgetItem(paciente["obra_social"]))
                self.listado_turnos.setItem(row_position, 5, QTableWidgetItem(paciente["fecha_turno"]))
        
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

    @pyqtSlot()
    def llamar_paciente(self):
        # Aquí puedes definir la acción para llamar a un paciente.
        # Por ejemplo, obtener el nombre del paciente de la primera fila seleccionada.
        row = self.listado_turnos.currentRow()
        if row >= 0:
            nombre_paciente = self.listado_turnos.item(row, 0).text()
            QMessageBox.information(self, "Llamar Paciente", f"Llamando a: {nombre_paciente}")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para llamar.")

    @pyqtSlot()
    def atender_paciente(self):
        # Aquí puedes definir la acción para atender al paciente.
        # Por ejemplo, obtener el nombre del paciente de la primera fila seleccionada.
        row = self.listado_turnos.currentRow()
        if row >= 0:
            nombre_paciente = self.listado_turnos.item(row, 0).text()
            QMessageBox.information(self, "Atender Paciente", f"Atendiendo a: {nombre_paciente}")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para atender.")

    @pyqtSlot()
    def ver_todos_pacientes(self):
        # Aquí puedes mostrar todos los pacientes en una nueva ventana o realizar cualquier acción adicional.
        self.cargar_turnos()  # Esto recarga la lista de pacientes en la tabla
