import unittest
from src.gramatica import Gramatica

class GramaticaTest(unittest.TestCase):
    
    def setUp(self):
        self.gramatica = Gramatica()
        
    
    def test_estandar(self):
        cadena = "Yo creo que el final puede mejorar con la propuesta de agregar mascotas"
        self.assertTrue(self.gramatica.validar_cadena(cadena))
    
    def test_limite(self):
        cadena = ""
        self.assertFalse(self.gramatica.validar_cadena(cadena))

    def test_limite2(self):
        cadena = "Yo"
        self.assertFalse(self.gramatica.validar_cadena(cadena))

    def test_interesante(self):
        cadena = "Yo puede mejorar"
        self.assertFalse(self.gramatica.validar_cadena(cadena))    


if __name__ == '__main__':
    unittest.main()
