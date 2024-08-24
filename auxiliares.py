from PySide6.QtWidgets import QDialog, QVBoxLayout, QDialogButtonBox, QLabel

import sys
from PySide6.QtWidgets import QApplication, QDialog, QLabel, QPushButton, QVBoxLayout


class Popup(QDialog):
    def __init__(self, titulo, mensaje):
        super().__init__()
        self.setWindowTitle(titulo)
        self.layout = QVBoxLayout()
        self.label = QLabel(mensaje)
        self.layout.addWidget(self.label)
        self.boton = QPushButton("Aceptar")
        self.boton.clicked.connect(self.accept)
        self.layout.addWidget(self.boton)
        self.setLayout(self.layout)


class VentanaErrorCalculoFabricacion(Popup):
    def __init__(self):
        super().__init__("Error", "Repase los datos introducidos.")


class VentanaErrorSeleccion(Popup):
    def __init__(self):
        super().__init__("Error", "Tiene que elegir una opción.")


class VentanaFaltanDatos(Popup):
    def __init__(self):
        super().__init__("Error: Faltan datos", "Por favor, complete todos los campos.")


class VentanaCantidadSuperior(Popup):
    def __init__(self):
        super().__init__("Error: Cantidad superior",
                         "La cantidad ingresada es superior a la permitida.")


class VentanaNumeroEntero(Popup):
    def __init__(self):
        super().__init__("Error", "Comprueba la cantidad a fabricar. La cantidad debe ser un número entero.")


class VentanaComponentesVacio(Popup):
    def __init__(self):
        super().__init__("Error", "La cantidad no puede estar vacia.")


class VentanaDivisionCero(Popup):
    def __init__(self):
        super().__init__("Error", "No se puede dividir entre cero.")