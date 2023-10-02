import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QStackedWidget
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class FlorkWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Flork Life Decisions")
        self.setGeometry(100, 100, 900, 700)
        background = QLabel(self)
        background.setGeometry(0, 0, 900, 700)
        pixmap = QPixmap('assets/images/bg.png')
        background.setPixmap(pixmap)
        background.setStyleSheet("border: none;")
        self.stacked_widget = QStackedWidget(self)

        # Página 1: Introducción y entrada del nombre
        self.page_intro = self.create_intro_page()
        self.stacked_widget.addWidget(self.page_intro)

        # Página 2: Juego
        self.page_juego = self.create_description_game_page()
        self.stacked_widget.addWidget(self.page_juego)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def create_intro_page(self):
        page = QWidget()

        text_label = QLabel("FLORK LIFE DECISIONS", page)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont("Gill Sans MT Condensed", 70))
        text_label.setGeometry(0, 110, 900, 100)
        text_label.setStyleSheet("color: black; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;")

        label_nombre = QLabel("Ingresa tu nombre", page)
        label_nombre.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_nombre.setFont(QFont("Gill Sans MT Condensed", 30))
        label_nombre.setGeometry(0, 250, 900, 60)
        label_nombre.setStyleSheet("color: black;")

        self.input_nombre = QLineEdit(page)
        self.input_nombre.setFont(QFont("Gill Sans MT Condensed", 20))
        self.input_nombre.setGeometry(300, 320, 300, 40)

        boton_jugar = QPushButton("Jugar", page)
        boton_jugar.setFont(QFont("Gill Sans MT Condensed", 20))
        boton_jugar.setGeometry(350, 450, 200, 50)
        boton_jugar.setStyleSheet("background-color: #FF3B41; color: white;")
        boton_jugar.clicked.connect(self.validar_nombre)

        return page

    def create_description_game_page(self):
        page = QWidget()
        
        text_label = QLabel("FLORK LIFE DECISIONS", page)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont("Gill Sans MT Condensed", 70))
        text_label.setGeometry(0, 110, 900, 100)
        text_label.setStyleSheet("color: black; text-shadow: -1px -1px 0 black, 1px -1px 0 black, -1px 1px 0 black, 1px 1px 0 black;")

        return page

    def validar_nombre(self):
        nombre = self.input_nombre.text()
        # Expresión regular para validar que el nombre solo contenga letras
        patron = r'^[a-zA-Z]+$'
        if re.match(patron, nombre):
            # Cambiar a la página del juego
            self.stacked_widget.setCurrentWidget(self.page_juego)
        else:
            # Mostrar mensaje de error si el nombre no cumple con el patrón
            QMessageBox.critical(self, "Error", "El nombre solo debe contener letras (a-z o A-Z).")

def create_window():
    app = QApplication(sys.argv)
    ventana = FlorkWindow()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    create_window()
