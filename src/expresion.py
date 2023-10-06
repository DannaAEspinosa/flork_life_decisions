import re

class Expresion:

    def __init__(self):
       self.expName = r'^[A-Z][a-zA-Z]{2,}$'
       self.expNewFinal =r'\b(Yo|creo|que|el|final|puede|mejorar|con)\b'
       
    def validateName(self, name):
        return re.match(self.expName,name)    

           
    def validateFinal(self, cadena):
        return re.findall(self.expNewFinal, cadena)      

    



    


