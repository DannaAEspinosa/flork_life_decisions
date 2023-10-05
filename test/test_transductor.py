import unittest
from src.transductor import Transductor, init_transductor

class TransductorTest(unittest.TestCase):

    def setUp(self):
        self.transductorObj = Transductor()
        
    def test_estandar1(self):
        cadena = "Nvk"
        self.assertTrue("Soy"==self.transductorObj.translateDialog(cadena)[0])
    def test_estandar2(self):
        cadena = "Nvk"
        self.assertTrue("Soy"== init_transductor(cadena))
    
    def test_limite1(self):
        cadena = " "
        self.assertTrue([] == self.transductorObj.translateDialog(cadena))

    def test_limite2(self):
        cadena = " "
        self.assertTrue(""== init_transductor(cadena))
    
    def test_interesante1(self):
        cadena = "Nk o oev o"
        self.assertFalse("Soy"==self.transductorObj.translateDialog(cadena))

    def test_interesante2(self):
        cadena = "Nk o oev o"
        self.assertFalse("Soy"== init_transductor(cadena))    
    

