import json

class Paciente:
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.dni = ""
        self.telefono = ""
        self.obra_social = ""
        self.archivo_json = "datos/pacientes.json"

    def consultarDatosPaciente(self):
        return {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "dni": self.dni,
            "telefono": self.telefono,
            "obra_social": self.obra_social
        }

    def crearPaciente(self, nombre, apellido, dni, telefono, obra_social):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
        self.obra_social = obra_social


    def registrarPaciente(self):
        # Se lee el archivo JSON y se agrega el nuevo paciente
        try:
            with open(self.archivo_json, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {"pacientes": []}  # Si el archivo no existe, se crea la estructura inicial

        # Agregamos el nuevo paciente a la lista de pacientes
        data["pacientes"].append(self.consultarDatosPaciente())

        # Guardamos los datos actualizados en el archivo JSON
        try:
            with open(self.archivo_json, 'w') as file:
                json.dump(data, file, indent=4)
                return True

        except Exception as e:
            print(f"Error al crear el archivo JSON: {e}")
            return False


    def buscarPaciente(self, dni_buscado):
        try:
            # Abrimos y cargamos el archivo JSON
            with open(self.archivo_json, "r") as archivo:
                datos = json.load(archivo)
            
            # Iteramos sobre la lista de pacientes para buscar el DNI
            for paciente in datos.get("pacientes", []):
                if paciente["dni"] == dni_buscado:
                    return paciente  # Retorna el paciente encontrado
            
            # Si no se encuentra el paciente
            return None
        
        except FileNotFoundError:
            print(f"Error: El archivo '{self.archivo_json}' no se encontró.")
        except json.JSONDecodeError:
            print(f"Error: El archivo '{self.archivo_json}' tiene un formato inválido.")
        except Exception as e:
            print(f"Error inesperado: {e}")
