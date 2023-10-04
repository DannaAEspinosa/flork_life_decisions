from pyformlang.cfg import Variable, Terminal, Production, CFG

import random

# Definición de variables y terminales
S = Variable('S')  # Variable inicial
A = Variable('A')
B = Variable('B')
quien_eres = Terminal('¿Quién eres?')
detente_hablame = Terminal('¡Detente! ¡Háblame en un idioma que pueda entender!')

respuestas_figura = [
    "¿Blorom tokum? Kilum dorblor osklor blorbor, tiklor susklor deklor blorfor klorlor.",
    "¿Blorom tokum? Dorblorlor gorklan deklorlor dorbloromos antikluglos, eltor tiklorstiglor deklorlor pesklor osklor.",
]

from pyformlang.cfg import CFG

gramatica_state18 = CFG.from_text("""
S -> A B
A -> '¿Quién eres?' | '¡Detente! ¡Háblame en un idioma que pueda entender!'
B -> '{}'
""".format('|'.join(respuestas_figura)))

print(gramatica_state18.contains('¿Quién eres?'))
print(gramatica_state18.contains('¡Detente! ¡Háblame en un idioma que pueda entender!'))
print(gramatica_state18.contains(random.choice(respuestas_figura)))



# Llamar a la función para generar un diálogo aleatorio


if __name__ == '__main__':
    dialogo_generador()

