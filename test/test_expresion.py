import unittest
import sys
import src.expresion
#from src.expresion import Expresion

class ExpresionTest(unittest.TestCase):

    def setUp(self):
        self.expresion = src.expresion.Expresion()

    def test_estandar1(self):
        cadena = "JohnDue"
        self.assertTrue(self.expresion.validateName(cadena))
    
    def test_estandar2(self):
        cadena = "Yo"
        self.assertTrue(self.expresion.validateFinal(cadena))
    
    def test_limite1(self):
        cadena = "A"
        self.assertFalse(self.expresion.validateName(cadena))
    
    def test_limite2(self):
        cadena = ""
        self.assertFalse(self.expresion.validateFinal(cadena))
    
    def test_interesante1(self):
        cadena = "John-Due"
        self.assertFalse(self.expresion.validateName(cadena))
    
    def test_interesante2(self):
        cadena = "CREO"
        self.assertTrue(self.expresion.validateName(cadena))
    