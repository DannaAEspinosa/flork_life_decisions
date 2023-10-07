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
    
    def test_limite1(self):
        cadena = " "
        self.assertTrue([] == self.transductorObj.translateDialog(cadena))
    
    def test_interesante1(self):
        cadena = "Nk o oev o"
        self.assertFalse("Soy"==self.transductorObj.translateDialog(cadena))
   
    

