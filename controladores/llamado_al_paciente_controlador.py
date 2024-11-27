import json
import serial
import time
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from interfaces.llamado_al_paciente import Ui_MainWindow
from controladores.todos_los_pacientes_controlador import verPacientes
from controladores.atencionalpaciente_controlador import AtencionPaciente
from clases.class_paciente import Paciente

class AtencionPacienteWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cargarTurnos()
    
    def cargarTurnos(self):
        try:
            with open("datos/turnos.json", "r") as file:
                turnos = json.load(file)

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

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

    def llamarPaciente(self):
        # Obtener la fila seleccionada
        row = self.listado_turnos.currentRow()
        
        if row >= 0:  # Verifica que haya una fila seleccionada
            nombre_paciente = self.listado_turnos.item(row, 0).text()  # Obtiene el nombre del paciente en la primera columna

            # Mostrar mensaje de información al usuario
            QMessageBox.information(self, "Llamar Paciente", f"Llamando a: {nombre_paciente}")
            
            # Llamar al Arduino para mostrar el nombre del paciente durante algunos segundos
            self.enviarAlArduino(nombre_paciente, segundos=5)  # Puedes cambiar el valor de segundos si es necesario

        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para llamar.")

    def enviarAlArduino(self, nombre_paciente, segundos=5):
        try:
            # Conectar al puerto serie (ajustar el puerto según sea necesario)
            self.arduino = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=1)  # Cambia el puerto si es necesario
            print(f"Enviando al Arduino: {nombre_paciente}")
            
            # Enviar el nombre del paciente al Arduino con un salto de línea
            self.arduino.write(f"{nombre_paciente}\n".encode())
            
            # Espera los segundos dados para mantener el mensaje visible en Arduino
            time.sleep(segundos)

        except Exception as e:
            print(f"Error al enviar al Arduino: {e}")

        finally:
            if hasattr(self, 'arduino') and self.arduino.is_open:
                self.arduino.close()

    def atenderPaciente(self):
        # Se atiende al paciente seleccionado.
        row = self.listado_turnos.currentRow()
        if row >= 0:
            # Creamos un objeto Paciente que nos servirá para buscar ese paciente y si no existe, 
            # guardarlo en el archivo JSON.
            paciente = Paciente()

            # Obtenemos los datos del paciente seleccionado para buscarlo por DNI en la base de pacientes (JSON Pacientes)
            nombre = self.listado_turnos.item(row, 0).text()
            apellido = self.listado_turnos.item(row, 1).text()
            dni = self.listado_turnos.item(row,2).text()
            telefono = self.listado_turnos.item(row, 3).text()
            obra_social = self.listado_turnos.item(row, 4).text()
            fecha_hora = self.listado_turnos.item(row, 5).text()

            if paciente.buscarPaciente(dni) == None:
                # El paciente no existe, es su primera atención por lo que hay que crearlo en la base de 
                # pacientes
                paciente.crearPaciente(nombre, apellido, dni, telefono, obra_social)
                paciente.registrarPaciente()

            # Se genera el objeto de Atención al Paciente para abrir dicha ventana
            self.ventanaAtencionPaciente = AtencionPaciente(nombre, apellido, dni, telefono, obra_social, fecha_hora)
            self.ventanaAtencionPaciente.exec_()
            self.cargarTurnos()

        else:
            QMessageBox.warning(self, "Error", "Seleccione un turno para atender.")

    def abrirInfoPacientes(self):
        ventanaTurno = verPacientes()
        ventanaTurno.exec_()

    def salir(self):
        return super().close()

