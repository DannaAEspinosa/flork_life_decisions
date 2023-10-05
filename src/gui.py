import sys
import automata, expresion, gramatica
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout, QStackedWidget, QHBoxLayout,QSpacerItem, QSizePolicy, QGraphicsBlurEffect, QInputDialog, QDialog, QTextEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
from pyformlang.finite_automaton import Symbol

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
        self.page_juego = self.create_description_game_page("")
        self.stacked_widget.addWidget(self.page_juego)

        # Página 3: Después de hacer clic en "Estoy listo"
        self.page_ready = self.create_ready_page("",automata.Automata(""),automata.Automata("").estado_inicial)
        self.stacked_widget.addWidget(self.page_ready)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

    def create_intro_page(self):
        page = QWidget()

        text_label = QLabel("FLORK LIFE DECISIONS", page)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont("Gill Sans MT Condensed", 70))
        text_label.setGeometry(0, 110, 900, 100)
        text_label.setStyleSheet("color: black;")


        label_nombre = QLabel("Ingresa  nombre", page)

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
    
    def create_description_game_page(self, nombre):
        page = QWidget()
        
        layout = QVBoxLayout()

        text_label = QLabel("Descripción del juego", page)
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setFont(QFont("Gill Sans MT Condensed", 70))
        text_label.setStyleSheet("color: #FF3B41")

        # Establecer un ancho fijo para el text_label
        text_label.setFixedWidth(800)

        # Recuadro de color blanco en el centro
        white_box = QLabel()
        white_box.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinea el recuadro al centro horizontalmente
        white_box.setStyleSheet("background-color: white; border: 2px solid #FF3B41")
        white_box.setFixedWidth(600)
        white_box.setFixedHeight(400)

        # Botón "Iniciar" en la parte central de abajo
        iniciar_button = QPushButton("ESTOY LIST@", page)
        iniciar_button.setFont(QFont("Gill Sans MT Condensed", 20))
        iniciar_button.setStyleSheet("background-color: #FF3B41; color: white;")
        iniciar_button.clicked.connect(lambda: self.startGame(nombre))
        # Texto dentro del recuadro
        texto = f"¡Hola {nombre}, te damos la bienvenida a FLORK DECISIONS LIFE! En este emocionante juego, te sumergirás en el fascinante mundo de Flork {nombre}, un personaje lleno de curiosidad y valentía que se enfrenta a una serie de desafíos y decisiones que afectarán su destino. \n\nTú eres el narrador de su historia y, en cada paso del camino, deberás tomar decisiones cruciales que influirán en el rumbo de sus aventuras. \n\nCONTROLES: \nPara poder tomar una decisión podrás teclear la letra correspondiente a cada opción (a, b o c) o simplemente darle click a la opción deseada. \n\nAhora sí ¿Estás listo para empezar?"

        descp_label = QLabel(texto, white_box)  # Agrega white_box como padre de descp_label
        descp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Alinea el texto al centro vertical y horizontalmente
        descp_label.setFont(QFont("Gill Sans MT Condensed", 15))
        descp_label.setStyleSheet("color: black;")
        descp_label.setWordWrap(True)


        # Agregar elementos al layout principal
        layout.addWidget(text_label, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(white_box, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(iniciar_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        white_box_layout = QVBoxLayout()
        white_box_layout.addWidget(descp_label)
        white_box.setLayout(white_box_layout)

        # Configurar el QVBoxLayout en la ventana
        page.setLayout(layout)
        return page


    def create_situation_inicial_game(self,nombre):
        page=QWidget()

        return page

    def create_ready_page(self,n,aut,estadoActual):
        page = QWidget()
        # Crear un widget secundario para aplicar el efecto de desenfoque
        blur_widget = QWidget(page)
        blur_widget.setStyleSheet("background-color: rgba(255, 255, 255, 100);")  # Fondo semitransparente
        blur_widget.setFixedSize(900, 700)  # Tamaño que cubre la página "listo"

        # Aplicar un efecto de desenfoque al widget secundario
        blur_effect = QGraphicsBlurEffect()
        blur_effect.setBlurRadius(10)  # Ajusta el radio de desenfoque según lo desees
        blur_widget.setGraphicsEffect(blur_effect)
        layout = QVBoxLayout()
         # Crear un widget secundario para aplicar el efecto de desenfoque
        top_layout=QHBoxLayout()
        # Rectángulo de color en la parte superior
        top_rect = QLabel(aut.estado_texto[estadoActual])
        top_rect.setFixedWidth(700)
        top_rect.setFixedHeight(200)
        top_rect.setAlignment(Qt.AlignmentFlag.AlignCenter )
        top_rect.setStyleSheet("background-color: #FF3B41")
        top_rect.setFont(QFont("Gill Sans MT Condensed", 12))
        top_rect.setWordWrap(True)
        top_rect.setMargin(10)
        top_layout.addWidget(top_rect)

        center_layout=QHBoxLayout()
        # Imagen en el centro
        image_label = QLabel(page)
        image_label.setFixedWidth(700)
        image_label.setFixedHeight(300)
        pixmap = QPixmap(aut.estado_image[estadoActual])  # Reemplaza 'your_image.png' con la ruta de tu imagen
        image_label.setPixmap(pixmap)

        
        center_layout.addWidget(image_label)


        # División en dos recuadros en la parte inferior
        if estadoActual not in aut.estado_aceptacion:
            bottom_layout=QHBoxLayout()
            left_layout = QHBoxLayout()
            center2_layout = QHBoxLayout()
            right_layout = QHBoxLayout()

            left_bottom_rect = QPushButton()
            if estadoActual == aut.estado_inicial: 
                left_bottom_rect.setFixedWidth(270)
                left_bottom_rect.setFixedHeight(100)
            else:
                left_bottom_rect.setFixedWidth(350)
                left_bottom_rect.setFixedHeight(100)
            left_bottom_rect.setStyleSheet("background-color: #C93431")
            estado_actualA = self.elegirOpcion(aut,estadoActual,Symbol("a"))
            left_bottom_rect.clicked.connect(lambda: self.change_page(n,aut,estado_actualA))

            center_bottom_rect = QPushButton()
            if estadoActual == aut.estado_inicial: 
                center_bottom_rect.setFixedWidth(270)
                center_bottom_rect.setFixedHeight(100)
            else:
                center_bottom_rect.setFixedWidth(350)
                center_bottom_rect.setFixedHeight(100)
            
            center_bottom_rect.setStyleSheet("background-color: #C93431")
            estado_actualB = self.elegirOpcion(aut,estadoActual,Symbol("b"))

            center_bottom_rect.clicked.connect(lambda: self.change_page(n,aut,estado_actualB))

            if estadoActual == aut.estado_inicial: 
                right_bottom_rect = QPushButton()
                right_bottom_rect.setFixedWidth(270)
                right_bottom_rect.setFixedHeight(100)
                right_bottom_rect.setStyleSheet("background-color: #C93431")
                estado_actualC = self.elegirOpcion(aut,estadoActual,Symbol("c"))
                right_bottom_rect.clicked.connect(lambda: self.change_page(n,aut,estado_actualC))

            # Agregar imagen a la izquierda de cada botón
            
            simboloA=Symbol("a")
            transicionA=(estadoActual,simboloA)
            left_image = QLabel()
            left_image.setFixedWidth(65)
            left_image.setFixedHeight(90)
            left_image.setPixmap(QPixmap('assets/images/a.png'))  # Reemplaza 'left_image.png' con la ruta de tu imagen
            left_lb = QLabel(aut.texto_transiciones[transicionA])
            left_lb.setFont(QFont("Gill Sans MT Condensed", 10))
            left_lb.setWordWrap(True)
            left_layout.addWidget(left_image)
            left_layout.addWidget(left_lb)
            left_bottom_rect.setLayout(left_layout)
            
            simboloB=Symbol("b")
            transicionB=(estadoActual,simboloB)
            center_image = QLabel()
            center_image.setFixedWidth(65)
            center_image.setFixedHeight(80)
            center_image.setPixmap(QPixmap('assets/images/b.png'))  # Reemplaza 'center_image.png' con la ruta de tu imagen
            center_lb = QLabel(aut.texto_transiciones[transicionB])
            center_lb.setFont(QFont("Gill Sans MT Condensed", 10))
            center_lb.setWordWrap(True)
            center2_layout.addWidget(center_image)
            center2_layout.addWidget(center_lb)
            center_bottom_rect.setLayout(center2_layout)
            
            if estadoActual == aut.estado_inicial: 
                simboloC=Symbol("c")
                transicionC=(estadoActual,simboloC)
                right_image = QLabel()
                right_image.setFixedWidth(65)
                right_image.setFixedHeight(80)
                right_image.setPixmap(QPixmap('assets/images/c.png'))  # Reemplaza 'right_image.png' con la ruta de tu imagen
                right_lb = QLabel(aut.texto_transiciones[transicionC])
                right_lb.setFont(QFont("Gill Sans MT Condensed", 10))
                right_lb.setWordWrap(True)
                right_layout.addWidget(right_image)
                right_layout.addWidget(right_lb)
                right_bottom_rect.setLayout(right_layout)


            # Agregar rectángulos al layout principal
            bottom_layout.addWidget(left_bottom_rect, alignment=Qt.AlignmentFlag.AlignCenter)
            bottom_layout.addWidget(center_bottom_rect, alignment=Qt.AlignmentFlag.AlignCenter)
            if estadoActual == aut.estado_inicial: 
                bottom_layout.addWidget(right_bottom_rect, alignment=Qt.AlignmentFlag.AlignCenter)
            
                    
            # Agregar elementos al layout principal
            layout.addLayout(top_layout)
            layout.addLayout(center_layout)
            layout.addLayout(bottom_layout)
        else:
            x=QHBoxLayout()

            left_bottom_rect = QLabel("Haz llegado al final de la historia")
            left_bottom_rect.setFixedWidth(270)
            left_bottom_rect.setFixedHeight(30)
            left_bottom_rect.setStyleSheet("background-color: white")
            left_bottom_rect.setFont(QFont("Gill Sans MT Condensed", 15))
            left_bottom_rect.setWordWrap(True)

            x.addWidget(left_bottom_rect, alignment=Qt.AlignmentFlag.AlignCenter)
            
            bottom_layout=QHBoxLayout()
            
            r_button_rect = QPushButton("Sugerir otro final")
            r_button_rect.setFixedWidth(270)
            r_button_rect.setFixedHeight(90)
            r_button_rect.setStyleSheet("background-color: #C93431")
            r_button_rect.setFont(QFont("Gill Sans MT Condensed", 15))

            r_button_rect.clicked.connect(self.nuevoFinal)

            left_button_rect = QPushButton("Volver a jugar")
            left_button_rect.setFixedWidth(270)
            left_button_rect.setFixedHeight(90)
            left_button_rect.setStyleSheet("background-color: #C93431")
            left_button_rect.setFont(QFont("Gill Sans MT Condensed", 15))

            left_button_rect.clicked.connect(lambda: self.startGame(self.restartName(n)))

            bottom_layout.addWidget(r_button_rect, alignment=Qt.AlignmentFlag.AlignCenter)
            bottom_layout.addWidget(left_button_rect, alignment=Qt.AlignmentFlag.AlignCenter)

            layout.addLayout(top_layout)
            layout.addLayout(center_layout)
            layout.addLayout(x)
            layout.addLayout(bottom_layout)


        # Configurar el QVBoxLayout en la ventana
        page.setLayout(layout)

        return page
    
    def change_page(self, n,aut, estadoActual):
        self.page_ready = self.create_ready_page(n,aut, estadoActual)
        self.stacked_widget.addWidget(self.page_ready)
        self.stacked_widget.setCurrentWidget(self.page_ready)

    def restartName(self, n):
        while True:

            reply = QMessageBox.question(self, 'Reiniciar juego', '¿Desea cambiar el nombre de Flork?', QMessageBox.Yes | QMessageBox.No)
        

            if reply == QMessageBox.Yes:
                new_name, ok = QInputDialog.getText(self, 'Cambiar Nombre', 'Ingrese un nuevo nombre:')
                if ok:
                    exp = expresion.Expresion()
                    if exp.validateName(new_name):
                        n = new_name
                        break 
                    else:
                        QMessageBox.critical(self, "Error", "La cadena debe cumplir con las siguientes condiciones: \n\n*Solo se aceptan letras (a-z o A-Z). \n*La primer letra debe ser mayúscula (A-Z). \n*La longitud de la cadena debe ser mayor a 2 caracteres. \n\nEjemplo: (Diana, Carlos, Danna)")
                else:
                    break  # Si el usuario cancela
            else:
                
                break  # Si el usuario no quiere cambiar el nombre
        return n

        

    def startGame(self,nombre):
        aut = automata.Automata("Flork "+nombre)
        estado_actual = aut.estado_inicial
        self.page_ready = self.create_ready_page(nombre,aut,estado_actual)
        self.stacked_widget.addWidget(self.page_ready)
        self.stacked_widget.setCurrentWidget(self.page_ready)


    def validar_nombre(self):
        nombre = self.input_nombre.text()
        # Expresión regular para validar que el nombre solo contenga letras
        exp=expresion.Expresion()
        if exp.validateName(nombre):
            # Cambiar a la página del juego
            self.page_juego = self.create_description_game_page(nombre)
            self.stacked_widget.addWidget(self.page_juego)
            self.stacked_widget.setCurrentWidget(self.page_juego)
        else:
            # Mostrar mensaje de error si el nombre no cumple con el patrón
            QMessageBox.critical(self, "Error", "La cadena debe cumplir con las siguientes condiciones: \n\n*Solo se aceptan letras  (a-z o A-Z). \n*La primer letra debe ser mayúscula (A-Z). \n*La longitud de la cadena debe ser mayor a 2 caracteres. \n\nEjemplo: (Diana, Carlos, Danna)")
    
    def elegirOpcion(self,aut,estadoAct, simboloElegido):
        transicionElegida = (estadoAct, simboloElegido)
        if transicionElegida in aut.transiciones:
            estadoAct = aut.transiciones[transicionElegida]
        return estadoAct
    

    def nuevoFinal(self):
        dialog = NuevoFinalDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            nuevo_final = dialog.text_edit.toPlainText()

class NuevoFinalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sugerir otro final")
        self.setLayout(QVBoxLayout())

        self.label = QLabel("Ingrese un nuevo final:", self)
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Yo creo que el final puede mejorar con...")
        self.accept_button = QPushButton("Enviar", self)
        self.accept_button.clicked.connect(self.validar_final)

        self.layout().addWidget(self.label)
        self.layout().addWidget(self.text_edit)
        self.layout().addWidget(self.accept_button)


    def validar_final(self):
            new_final = self.text_edit.toPlainText()
            gr = gramatica.Gramatica()
            if gr.validar_cadena(new_final):
                QMessageBox.accept(self, "Final aceptado exitosamente", "¡Gracias por tu sugerencia, Esto nos ayudará a crear historias  más geniales!")
                self.accept()  # Cerrar el cuadro de diálogo si el final es válido
            else:
                reply = QMessageBox.critical(self, "Error", "El final sugerido no cumple con la gramática establecida ya que debe empezar con la cadena 'Yo creo que el final puede mejorar con '. ¿Desea seguir editando?",
                                            QMessageBox.Yes | QMessageBox.No)
                if reply == QMessageBox.No:
                    self.reject()  # Cerrar el cuadro de diálogo si el usuario elige no seguir editando

def create_window():
    app = QApplication(sys.argv)
    ventana = FlorkWindow()
    ventana.show()
    sys.exit(app.exec_())


    

if __name__ == '__main__':
    create_window()
