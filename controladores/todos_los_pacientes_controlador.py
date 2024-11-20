from interfaces.todos_los_pacientes import Ui_historialDePacientes
from PyQt5.QtWidgets import QDialog

class verPacientes(QDialog, Ui_historialDePacientes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)