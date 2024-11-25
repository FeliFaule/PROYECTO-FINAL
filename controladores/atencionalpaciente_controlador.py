from interfaces.atencionalpaciente import Ui_atencionalpaciente
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMessageBox
import json
from clases.class_paciente import Paciente
from clases.class_turno import Turno
from datetime import datetime
import os


class AtencionPaciente(QDialog, Ui_atencionalpaciente):
    def __init__(self, nombre, apellido, dni, telefono, obra_social, fecha_hora):
        super().__init__()
        self.setupUi(self)

        self.label_dato_nombre.setText(nombre)
        self.label_dato_apellido.setText(apellido)
        self.label_dato_dni.setText(dni)
        self.label_dato_telefono.setText(telefono)
        self.label_dato_obra_social.setText(obra_social)
        self.fecha_hora_turno = fecha_hora

        self.archivo_json = "datos/historia_clinica.json"

        self.cargarHistoriaClinica()

        self.textEdit_motivo_consulta.setFocus()

    
    def cargarHistoriaClinica(self):
        # Creamos un objeto Paciente que nos servirá para buscar ese paciente y si no existe, 
        # guardarlo en el archivo JSON.
        paciente = Paciente()

        if paciente.buscarPaciente(self.label_dato_dni.text()):
            try:
                # Abrimos el archivo de Historia Clinica para buscar al paciente
                with open(self.archivo_json, "r") as file:
                    hc = json.load(file)

                # Buscamos al paciente por su DNI para ver si tiene visitas anteriores
                datos = next((p for p in hc["pacientes"] if p["dni"] == self.label_dato_dni.text()), None)

                if datos is None:
                    return
                
                # Si no salió a este punto significa que encontró al paciente
                self.textBrowser_historial.clear()

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


    
    def Volver(self):
        return super().close()
    
    
    def finalizarAtencion(self):
        # Se le advierte al usuario que si finaliza la atención sin hacer una receta no podra volver a hacerla.
        # Se le pide confirmación.
        respuesta = QtWidgets.QMessageBox.question(self, "Finalizar Atención", "Al finalizar la atención ya no podra generar una receta. ¿Deseas continuar?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
            QtWidgets.QMessageBox.No
        )

        # Procesar la respuesta del usuario
        if respuesta == QtWidgets.QMessageBox.No:
            return
        
        # Si decide continuar debemos registrar la visita medica para ese paciente en el archivo JSON.
        nueva_visita = {
            "fecha": datetime.now().strftime('%d-%m-%Y'),
            "motivo_consulta": self.textEdit_motivo_consulta.toPlainText(),
            "anamnesis": self.textEdit_anamnesis.toPlainText(),
            "indicaciones": self.textEdit_indicaciones.toPlainText()
        }
        
        # Estructura mínima del archivo JSON si no existe
        estructura_base = {
            "pacientes": []
        }
        
        # Verificar si el archivo existe
        if not os.path.exists(self.archivo_json):
            with open(self.archivo_json, "w") as archivo:
                json.dump(estructura_base, archivo, indent=4)
        
        # Cargar el archivo JSON
        try:
            with open(self.archivo_json, "r") as archivo:
                data = json.load(archivo)

        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de historia clínica.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar la historia clínica: {e}")
        
        # Buscar el paciente por DNI
        paciente_encontrado = None
        for paciente in data["pacientes"]:
            if paciente["dni"] == self.label_dato_dni.text():
                paciente_encontrado = paciente
                break
        
        if paciente_encontrado:
            # Si el paciente ya está registrado, agregar la nueva visita.
            paciente_encontrado["historia_clinica"].append(nueva_visita)
        else:
            # Si el paciente no está registrado, agregarlo con la nueva visita.
            nuevo_paciente = {
                "dni": self.label_dato_dni.text(),
                "historia_clinica": [nueva_visita]
            }
            data["pacientes"].append(nuevo_paciente)
        
        # Guardar los cambios en el archivo JSON.
        try:
            with open(self.archivo_json, "w") as archivo:
                json.dump(data, archivo, indent=4)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al guardar la historia clínica: {e}")

        # Eliminamos el turno del archivo JSON de Turnos
        turno = Turno()
        turno.eliminarTurno(self.label_dato_dni.text(), self.fecha_hora_turno)

        return super().close()

    
    def Recetar(self):
        pass