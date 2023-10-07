import unittest
import src.automata
#from src.automata import Automata
from pyformlang.finite_automaton import Symbol, State

class AutomataTest(unittest.TestCase):

    def setUp(self):
        self.automata = src.automata.Automata("Carlos")

    def test_estandar(self):
        #la cadena de opciones a probar en este caso es "ab". 
        estado1=(State("q0"),Symbol("a"))
        estado2 = (self.automata.transiciones[estado1],Symbol("b"))
        final = self.automata.transiciones[estado2]
        self.assertTrue(final==State("q3"))

    def test_limite1(self):
        #La cadena de opciones a probar en este caso es "bc".
        estado1 = (State("q0"),Symbol("b"))
        estado2 = (estado1,Symbol("c"))
        self.assertIsNone(self.automata.transiciones.get(estado2))
    
    def test_limite2(self):
        estado1= (State("q0"),Symbol("b"))
        self.assertFalse(estado1[0] in self.automata.estado_aceptacion)

    def test_interesante(self):
        estado1=(State("q0"),Symbol("c"))
        estado2=(self.automata.transiciones[estado1],Symbol("a"))
        estado3=(self.automata.transiciones[estado2],Symbol("a"))
        estado4=(self.automata.transiciones[estado3],Symbol("c"))
        self.assertFalse(estado4[0] in self.automata.estado_aceptacion)

