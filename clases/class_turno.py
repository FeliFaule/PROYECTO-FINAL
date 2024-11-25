import json
from clases import class_paciente
from PyQt5.QtWidgets import QMessageBox

class Turno ():
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.dni = ""
        self.telefono = ""
        self.obra_social = ""
        self.fecha_hora = ""
        self.archivo_json = "datos/turnos.json"

    def consultarDatosTurno(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "telefono": self.telefono,
            "obra_social": self.obra_social,
            "fecha_hora": self.fecha_hora
        }

    def crearTurno(self, nombre, apellido, dni, telefono, obra_social, fecha_hora):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.obra_social = obra_social
        self.fecha_hora = fecha_hora


    def registrarTurno(self):
        # Leer el archivo JSON y agregar el nuevo turno
        try:
            with open(self.archivo_json, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"turno": []}  # Si el archivo no existe, creamos la estructura inicial

        # Agregar el nuevo turno a la lista de turnos
        data["turno"].append(self.consultarDatosTurno())

        # Guardar los datos actualizados en el archivo JSON
        try:
            with open(self.archivo_json, 'w') as file:
                json.dump(data, file, indent=4)
                return True

        except Exception as e:
            print(f"Error al crear el archivo JSON: {e}")
            return False
        
    def eliminarTurno(self, dni, fecha_hora):
        # Se elimina el turno porque ya ha sido atendido.
        try:
            with open(self.archivo_json, "r") as archivo:
                data = json.load(archivo)
                turnos = data["turno"]

        except FileNotFoundError:
            QMessageBox.critical(self, "Error", "El archivo de turnos no se encontró.")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Error", "Error en el formato del archivo de turnos.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Ocurrió un error al cargar los turnos: {e}")    
        
        # Nos quedamos con la estructura de todos los turnos que no coincidan con la fecha y DNI.
        turnos = [turno for turno in turnos if turno["dni"] != dni or turno["fecha_hora"] != fecha_hora]
        data["turno"] = turnos
        
        # Guardar los datos actualizados de vuelta al archivo JSON
        with open("datos/turnos.json", "w") as archivo:
            json.dump(data, archivo, indent=4)        
