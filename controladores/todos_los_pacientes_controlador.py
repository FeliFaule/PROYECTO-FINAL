from interfaces.todos_los_pacientes import Ui_historialDePacientes
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
import json
from clases.class_paciente import Paciente

class verPacientes(QDialog, Ui_historialDePacientes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.archivo_json_paciente = "datos/pacientes.json"
        self.archivo_json_hc = "datos/historia_clinica.json"
        self.cargarPacientes()


    def cargarPacientes(self):    
        try:
            with open(self.archivo_json_paciente, "r") as file:
                pacientes = json.load(file)

            # Limpiar la tabla antes de insertar nuevos datos
            self.listado_pacientes.setRowCount(0)  

            # Insertar los datos de los pacientes en la tabla
            for paciente in pacientes["pacientes"]:
                # Agregar una nueva fila en la tabla
                row_position = self.listado_pacientes.rowCount()
                self.listado_pacientes.insertRow(row_position)

                # Insertar los datos del paciente en las celdas correspondientes
                self.listado_pacientes.setItem(row_position, 0, QTableWidgetItem(paciente["nombre"]))
                self.listado_pacientes.setItem(row_position, 1, QTableWidgetItem(paciente["apellido"]))
                self.listado_pacientes.setItem(row_position, 2, QTableWidgetItem(paciente["dni"]))
                self.listado_pacientes.setItem(row_position, 3, QTableWidgetItem(paciente["obra_social"]))
      
        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de pacientes no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de pacientes.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los pacientes: {e}")

    
    def cargarHistoriaClinica(self):

        # Limpia los datos de detalle
        self.label_dato_nombre.setText("")
        self.label_dato_apellido.setText("")
        self.label_dato_dni.setText("")
        self.label_dato_telefono.setText("")
        self.label_dato_obra_social.setText("")
        self.textBrowser_historial.clear()



        # Obtenemos la fila seleccionada para tomar el DNI
        selected_row = self.listado_pacientes.currentRow()

        if not (selected_row >= 0):
            return
        else:
            dni_buscado = self.listado_pacientes.item(selected_row, 2).text()

        # Creamos un objeto Paciente que nos servirá para buscar ese paciente y si no existe, 
        # guardarlo en el archivo JSON.
        paciente = Paciente()
        self.datos_paciente = paciente.buscarPaciente(dni_buscado)

        if self.datos_paciente:
            # Seteamos los labels con los datos del paciente
            self.label_dato_nombre.setText(self.datos_paciente["nombre"])
            self.label_dato_apellido.setText(self.datos_paciente["apellido"])
            self.label_dato_dni.setText(self.datos_paciente["dni"])
            self.label_dato_telefono.setText(self.datos_paciente["telefono"])
            self.label_dato_obra_social.setText(self.datos_paciente["obra_social"])
            
            try:
                # Abrimos el archivo de Historia Clinica para buscar al paciente
                with open(self.archivo_json_hc, "r") as file:
                    hc = json.load(file)

                # Buscamos al paciente por su DNI para ver si tiene visitas anteriores
                datos = next((p for p in hc["pacientes"] if p["dni"] == dni_buscado), None)

                if datos is None:
                    return
                
                for evento in reversed(datos["historia_clinica"]):
                    # Formatear los datos del evento
                    texto_evento = (
                        f"Fecha: {evento['fecha']}\n"
                        f"Motivo de consulta: {evento['motivo_consulta']}\n"
                        f"Anamnesis: {evento['anamnesis']}\n"
                        f"Indicaciones: {evento['indicaciones']}\n"
                    )
                    # Insertar el evento en el QTextBrowser
                    self.textBrowser_historial.append(texto_evento)
                    self.textBrowser_historial.append("")  # Línea en blanco entre eventos

            except FileNotFoundError:
                self.textBrowser_historial.setPlainText("El archivo de historia clínica no se encontró.")
            except json.JSONDecodeError:
                self.textBrowser_historial.setPlainText("Error al leer el archivo JSON.")
            except Exception as e:
                self.textBrowser_historial.setPlainText(f"Ocurrió un error: {e}")               

    def salir(self):
        return super().close()
    
