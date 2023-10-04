from pyformlang.fst import FST

class Transductor: 
    def __init__(self):
        """
            "¿Blorom tokum?"
            "¿Quién eres?"    

            "Kilum dorblor osklor blorbor, tiklor susklor deklor blorfor klorlor."
             - Significado: "Soy el eco de tus peores pesadillas, el susurro de tus temores más profundos."   

            "Dorblorlor gorklan deklorlor dorbloromos antikluglos, eltor tiklorstiglor deklorlor pesklor osklor."
            - Significado: "Soy el guardián de secretos antiguos, el testigo de tus pecados ocultos." 
        """
        self.transducer = FST()

        self.transducer.add_transitions([
            ('q0','¿','q1','¿'),
            ('q1','B','q2','Q'),
            ('q2','l','q3','u'),
            ('q3','o','q4','i'),
            ('q4','r','q5','é'),
            ('q5','o','q6','n'),
            ('q6','m','q7',' '),
        ])
        self.transducer.add_start_state("q0")
        self.transducer.add_final_state("q100")

        
        
