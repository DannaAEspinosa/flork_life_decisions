import unittest
import sys
import src.transductor
#from src.transductor import Transductor, init_transductor

class TransductorTest(unittest.TestCase):

    def setUp(self):
        self.transductorObj = src.transductor.Transductor()
        
    def test_estandar1(self):
        cadena = "Nvk"
        self.assertTrue("Soy"==self.transductorObj.translateDialog(cadena)[0])
    def test_estandar2(self):
        cadena = "Nvk"
        self.assertTrue("Soy"== src.transductor.init_transductor(cadena))
    
    def test_limite1(self):
        cadena = " "
        self.assertTrue([] == self.transductorObj.translateDialog(cadena))

    def test_limite2(self):
        cadena = " "
        self.assertTrue(""== src.transductor.init_transductor(cadena))
    
    def test_interesante1(self):
        cadena = "Nk o oev o"
        self.assertFalse("Soy"==self.transductorObj.translateDialog(cadena))

    def test_interesante2(self):
        cadena = "Nk o oev o"
        self.assertFalse("Soy"== src.transductor.init_transductor(cadena))    
    

