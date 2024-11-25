import json
from interfaces.recepcionista_historialturnos import Ui_RecepcionistaMainWindow
from controladores.recepcionista_turnos_controlador import VentanaNuevoTurno
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QHeaderView
from datetime import datetime

class RecepcionistaWindow(QMainWindow, Ui_RecepcionistaMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargarTurnos(None)

    
    def cargarTurnos(self, turnos):
        # Si el parámetro de datos no viene con nada, entonces levanta los turnos del archivo
        if turnos == None:
            try:
                with open("datos/turnos.json", "r") as archivo:
                    contenido = json.load(archivo)
                    turnos = contenido["turno"]

            except FileNotFoundError:
                QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
            except json.JSONDecodeError:
                QMessageBox.critical(self, "Error", "Error en el formato del archivo de turnos.")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los turnos: {e}")
            
        # Limpiar la tabla antes de insertar nuevos datos
        self.tablaListaTurnos.setRowCount(0)  # Limpiar la tabla

        # Insertar los datos de los turnos obtenidos del archivo en la tabla
        for turno in turnos:
            # Agregar una nueva fila en la tabla
            row_position = self.tablaListaTurnos.rowCount()
            self.tablaListaTurnos.insertRow(row_position)

            # Insertar los datos del paciente en las celdas correspondientes
            self.tablaListaTurnos.setItem(row_position, 0, QTableWidgetItem(turno["nombre"]))
            self.tablaListaTurnos.setItem(row_position, 1, QTableWidgetItem(turno["apellido"]))
            self.tablaListaTurnos.setItem(row_position, 2, QTableWidgetItem(turno["dni"]))
            self.tablaListaTurnos.setItem(row_position, 3, QTableWidgetItem(turno["telefono"]))
            self.tablaListaTurnos.setItem(row_position, 4, QTableWidgetItem(turno["obra_social"]))
            self.tablaListaTurnos.setItem(row_position, 5, QTableWidgetItem(turno["fecha_hora"]))

        #self.tablaListaTurnos.resizeColumnsToContents()
        self.tablaListaTurnos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                

    
    def ordenarPorBurbuja(self, turnos):
        # Ordenamiento por burbuja basado en el horario.
        n = len(turnos)
        for i in range(n):
            for j in range(0, n-i-1):
                # Comparar horarios (convertirlos a datetime)
                hora1 = datetime.strptime(turnos[j]["fecha_hora"], "%d-%m-%Y %H:%M")
                hora2 = datetime.strptime(turnos[j+1]["fecha_hora"], "%d-%m-%Y %H:%M")
                if hora1 > hora2:
                    # Intercambiar si están desordenados
                    turnos[j], turnos[j+1] = turnos[j+1], turnos[j]
        return turnos

    
    def ordenarTurnos(self):
        # Ordena los datos usando el método de burbuja y recarga la tabla.
        # Primero obtenemos una lista con todos los elementos de la tabla
        lista_turnos = []

        for fila in range(self.tablaListaTurnos.rowCount()):
            turno = {
                "nombre": self.tablaListaTurnos.item(fila, 0).text(),
                "apellido": self.tablaListaTurnos.item(fila, 1).text(),
                "dni": self.tablaListaTurnos.item(fila, 2).text(),
                "telefono": self.tablaListaTurnos.item(fila, 3).text(),
                "obra_social": self.tablaListaTurnos.item(fila, 4).text(),
                "fecha_hora": self.tablaListaTurnos.item(fila, 5).text()
            }

            lista_turnos.append(turno)

        # Aplica el método de burbuja
        lista_turnos = self.ordenarPorBurbuja(lista_turnos)

        # Recargar la tabla con los datos ordenados
        self.cargarTurnos(lista_turnos)

    def salir(self):
        return super().close()
    
    def nuevoTurno(self):
        ventanaTurno = VentanaNuevoTurno()
        ventanaTurno.exec_()
        self.cargarTurnos(None)