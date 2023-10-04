from pyformlang.fst import FST

class Transductor: 
    def __init__(self):
        self.transducer = FST()

        self.transducer.add_transitions([
            # Soy
            ('q0', 'N', 'q1', ['S']),
            ('q1', 'v', 'q2', ['o']),
            ('q2', 'k', 'q3', ['y']),
            ('q3', ' ', 'q4', [' ']),
            # el
            ('q4', 'o', 'q5', ['e']),
            ('q5', 'd', 'q6', ['l']),
            ('q6', ' ', 'q7', [' ']),
            # eco
            ('q7', 'o', 'q8', ['e']),
            ('q8', 'e', 'q9', ['c']),
            ('q9', 'v', 'q10', ['o']),
            ('q10', ' ', 'q11', [' ']),
            # de
            ('q11', 'l', 'q12', ['d']),
            ('q12', 'o', 'q13', ['e']),
            ('q13', ' ', 'q14', [' ']),
            # tus
            ('q14', 'f', 'q15', ['t']),
            ('q15', 'r', 'q16', ['u']),
            ('q16', 'n', 'q17', ['s']),
            ('q17', ' ', 'q18', [' ']),
            # peores
            ('q18', 'r', 'q19', ['p']),
            ('q19', 'o', 'q20', ['e']),
            ('q20', 'v', 'q21', ['o']),
            ('q21', 'u', 'q22', ['r']),
            ('q22', 'o', 'q23', ['e']),
            ('q23', 'n', 'q24', ['s']),
            ('q24', ' ', 'q25', [' ']),
            # pesadillas
            ('q25', 'r', 'q26', ['p']),
            ('q26', 'o', 'q27', ['e']),
            ('q27', 'n', 'q28', ['s']),
            ('q28', 'b', 'q29', ['a']),
            ('q29', 'l', 'q30', ['d']),
            ('q30', 'z', 'q31', ['i']),
            ('q31', 'd', 'q32', ['l']),
            ('q32', 'd', 'q32', ['l']),
            ('q32', 'b', 'q35', ['a']),
            ('q35', 'n', 'q36', ['s']),
           
           
            
            
        ])
        self.transducer.add_start_state('q0')
        self.transducer.add_final_state('q3')
        self.transducer.add_final_state('q6')
        self.transducer.add_final_state('q10')
        self.transducer.add_final_state('q13')
        self.transducer.add_final_state('q17')
        self.transducer.add_final_state('q24')
        self.transducer.add_final_state('q36')
       

    def translateDialog(self,cadena):
        translation =(list(map(lambda x:
           "".join(x),list(self.transducer.translate(cadena)))))
        print(cadena)

        return translation
    
def init_application():
    # Crear una instancia del objeto Transductor
    transductor = Transductor()

    # Llamar a la función translate con una cadena de entrada
    cadena_entrada = 'Nvk od oev lo frn rovuon ronblzddbn'
    cadena_traducida = transductor.translateDialog(cadena_entrada)

    # Imprimir el resultado de la traducción
    traduccion = "".join(cadena_traducida)
    print("This is the translation:", traduccion)

if __name__ == '__main__':
    init_application()

    