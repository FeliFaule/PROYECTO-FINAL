import json
from PyQt5.QtWidgets import QMainWindow
from datetime import datetime
from recepcionista_turnos.py import Ui_MainWindow  # Importa el archivo .ui convertido a .py

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    self.botonguardar.clicked.connect(self.datos)
   
   
    def datos(self):
        pacientes= {
            
            "nombre"==self.editnombre.toPlainText(),
            "apellido"==self.editapellido.toPlainText(),
            "DNI"==self.editDNI.toPlainText(),
            "telefono"==self.edittelefono.toPlainText(),
            "obrasocial"==self.editobrasocial.toPlainText(),
            "fecha_hora" == self.Timeeditfecha.dateTime(),

        }

        try:
            with open("historial_pacientes.json", "r") as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []  

        
        existing_data.append(data)

        
        with open("historial_pacientes.json", "w") as file:
            json.dump(existing_data, file, indent=4)

        print("Datos guardados correctamente")

    if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
        
