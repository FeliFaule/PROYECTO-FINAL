import json
from clases import class_paciente

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