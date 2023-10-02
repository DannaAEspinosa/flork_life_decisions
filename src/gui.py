import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

# Variable global para almacenar el nombre válido
nombre_valido = ""

class FlorkWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flork Life Decisions")
        self.setGeometry(100, 100, 900, 700)

        # Fondo de la ventana
        background = QLabel(self)
        background.setGeometry(0, 0, 900, 700)
        pixmap = QPixmap('assets/images/bg.png')
        background.setPixmap(pixmap)

        # Texto en la parte central superior
        text_label = QLabel("FLORK LIFE DECISIONS", self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont("Gill Sans MT Condensed", 70))
        text_label.setGeometry(0, 110, 900, 100)
        text_label.setStyleSheet("color: black; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;")

        # Label "Ingresa tu nombre"
        label_nombre = QLabel("Ingresa tu nombre", self)
        label_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_nombre.setFont(QFont("Gill Sans MT Condensed", 30))
        label_nombre.setGeometry(0, 250, 900, 60)
        label_nombre.setStyleSheet("color: black;")

        # Cuadro de input
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setFont(QFont("Gill Sans MT Condensed", 20))
        self.input_nombre.setGeometry(300, 320, 300, 40)

        # Botón "Jugar"
        boton_jugar = QPushButton("Jugar", self)
        boton_jugar.setFont(QFont("Gill Sans MT Condensed", 20))
        boton_jugar.setGeometry(350, 450, 200, 50)
        boton_jugar.setStyleSheet("background-color: #FF3B41; color: white;")

        # Conectar la señal clicked del botón a la función de validación
        boton_jugar.clicked.connect(self.validar_nombre)

    def validar_nombre(self):
        nombre = self.input_nombre.text()
        # Expresión regular para validar que el nombre solo contenga letras
        patron = r'^[a-zA-Z]+$'
        if re.match(patron, nombre):
            global nombre_valido
            nombre_valido = nombre
            # Aquí puedes hacer lo que necesites con el nombre válido
            print(f"Nombre válido: {nombre_valido}")
        else:
            # Mostrar mensaje de error si el nombre no cumple con el patrón
            QMessageBox.critical(self, "Error", "El nombre solo debe contener letras (a-z o A-Z).")

def create_window():
    app = QApplication(sys.argv)
    ventana = FlorkWindow()
    ventana.show()
    sys.exit(app.exec_())