from interfaces.recepcionista_turnos import Ui_modalNuevoTurno
from PyQt5.QtWidgets import QDialog

class VentanaNuevoTurno(QDialog, Ui_modalNuevoTurno):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close(self):
        return super().close()