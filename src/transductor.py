from pyformlang.fst import FST

class Transductor: 
    def __init__(self):
        self.transducer = FST()

        self.transducer.add_transitions([
            #muerte rep
            ('q0', 'X', 'q76', ['M']),
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

            ##New string
            #Soy tu padre
            #tu
            ('q4', 'f', 'q37', ['t']),
            ('q37', 'r', 'q38', ['u']),
            ('q38', ' ', 'q39', [' ']),
            #padre
            ('q39', 'r', 'q40', ['p']),
            ('q40', 'b', 'q41', ['a']),
            ('q41', 'l', 'q42', ['d']),
            ('q42', 'u', 'q43', ['r']),
            ('q43', 'o', 'q44', ['e']),
            #fantasma
            ('q39', 'h', 'q46', ['f']),
            ('q46', 'b', 'q47', ['a']),
            ('q47', 'y', 'q48', ['n']),
            ('q48', 'f', 'q49', ['t']),
            ('q49', 'b', 'q50', ['a']),
            ('q50', 'n', 'q51', ['s']),
            ('q51', 'x', 'q52', ['m']),
            ('q52', 'b', 'q53', ['a']),
            ('q53', ' ', 'q54', [' ']),
            #personal
            ('q54', 'r', 'q55', ['p']),
            ('q55', 'o', 'q56', ['e']),
            ('q56', 'u', 'q57', ['r']),
            ('q57', 'n', 'q58', ['s']),
            ('q58', 'v', 'q59', ['o']),
            ('q59', 'y', 'q60', ['n']),
            ('q60', 'b', 'q61', ['a']),
            ('q61', 'd', 'q62', ['l']),
            ('q62', ' ', 'q63', [' ']),
            #guardian
            ('q7', 'i', 'q64', ['g']),
            ('q64', 'p', 'q65', ['u']),
            ('q65', 'b', 'q66', ['a']),
            ('q66', 'u', 'q67', ['r']),
            ('q67', 'l', 'q68', ['d']),
            ('q68', 'z', 'q69', ['i']),
            ('q69', 'b', 'q70', ['a']),
            ('q70', 'y', 'q71', ['n']),
            ('q71', ' ', 'q11', [' ']),
            #la
            ('q14', 'd', 'q73', ['l']),
            ('q73', 'b', 'q74', ['a']),
            ('q74', ' ', 'q75', [' ']),
            #muerte
            ('q75', 'x', 'q76', ['m']),
            ('q76', 'p', 'q77', ['u']),
            ('q77', 'o', 'q78', ['e']),
            ('q78', 'u', 'q79', ['r']),
            ('q79', 'f', 'q80', ['t']),
            ('q80', 'o', 'q81', ['e']),
            ('q81', ' ', 'q82', [' ']),
            
            #la
            ('q3', ' ', 'q14', [' ']),
            
            
        ])
        #Soy el eco de tus peores pesadillas
        self.transducer.add_start_state('q0')
        self.transducer.add_final_state('q3')
        self.transducer.add_final_state('q6')
        self.transducer.add_final_state('q10')
        self.transducer.add_final_state('q13')
        self.transducer.add_final_state('q17')
        self.transducer.add_final_state('q24')
        self.transducer.add_final_state('q36')
        ##Soy tu padre
        #tu
        self.transducer.add_final_state('q38')
        #padre
        self.transducer.add_final_state('q44')
        ##Soy tu fantasma personal
        #fantasma
        self.transducer.add_final_state('q53')
        #personal
        self.transducer.add_final_state('q62')
        ##Soy el guardian de la muerte
        #guardian
        self.transducer.add_final_state('q71')
        #la
        self.transducer.add_final_state('q74')
        #muerte
        self.transducer.add_final_state('q81')

    def translateDialog(self,cadena):
        translation =(list(map(lambda x:
           "".join(x),list(self.transducer.translate(cadena)))))
        print(cadena)

        return translation
    

if __name__ == '__main__':
    t=Transductor()
    cadena_entrada = 'Nvk od oev lo frn rovuon ronblzddbn'
    c2='Nvk fr rbluo'
    c3='Nvk od ipbulzby lo db xpoufo'
    c4='Nvk fr hbyfbnxb rounvybd'
    c5 = 'Nvk db xpoufo'
    c='Xpoufo'
    t.translateDialog(c)

    