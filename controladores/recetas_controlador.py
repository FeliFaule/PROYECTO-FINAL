from PyQt5.QtWidgets import QDialog, QMessageBox
from interfaces.recetas import Ui_RecetaDialog
from reportlab.pdfgen import canvas
from datetime import datetime

class creacionReceta(Ui_RecetaDialog, QDialog):
    def __init__(self, dni):
        super().__init__()
        self.setupUi(self)
        self.tipo_farmaco_lineEdit.setText("")
        self.cantidad_farmaco_lineEdit.setText("")
        self.por_cuanto_lineEdit.setText("")        
        self.cada_cuanto_lineEdit.setText("") 
        self.dni = dni      
         

    def guardarReceta(self):
        # Obtener los datos de los QLineEdit
        tipo_farmaco = self.tipo_farmaco_lineEdit.text()
        cantidad_farmaco = self.cantidad_farmaco_lineEdit.text()
        por_cuanto = self.por_cuanto_lineEdit.text()
        cada_cuanto = self.cada_cuanto_lineEdit.text()

        
        # Validar que todos los campos estén llenos
        if not (tipo_farmaco and cantidad_farmaco and por_cuanto and cada_cuanto):
            QMessageBox.warning(self, "Advertencia", "Por favor, complete todos los campos.")
            return
        
        
        # Crear el archivo PDF
        nombre_pdf = f"Recetas/{self.dni}_" + datetime.now().strftime('%d-%m-%Y_%H-%M') + ".pdf"
        c = canvas.Canvas(nombre_pdf)
        c.drawString(100, 750, f"Tipo de Fármaco: {tipo_farmaco}")
        c.drawString(100, 730, f"Cantidad del Fármaco: {cantidad_farmaco}")
        c.drawString(100, 710, f"Por cuánto tiempo: {por_cuanto}")
        c.drawString(100, 690, f"Cada cuánto tiempo: {cada_cuanto}")
        c.save()

        # Mostrar mensaje de confirmación
        QMessageBox.information(self, "Éxito", "Receta guardada y abierta correctamente.")

        # Vuelve a la ventana de atención
        return super().close()


    def Cancelar(self):
        return super().close()
