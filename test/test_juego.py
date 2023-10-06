import unittest
import sys
import src.juego
#from src.juego import FlorkWindow,NuevoFinalDialog

class FlorkWindowTest(unittest.TestCase):

    def setUp(self):
        self.window=src.juego.FlorkWindow()

class NuevoFinalDialogTest(unittest.TestCase):

    def setUp(self):
        self.nFinal=src.juego.NuevoFinalDialog()
    