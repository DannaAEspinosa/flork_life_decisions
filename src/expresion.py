import re

class Expresion:

    def __init__(self):
       self.expName = r'^[A-Z][a-zA-Z]{2,}$'
       self.expNewFinal =r'\b(Yo|creo|que|el|final|puede|mejorar|con)\b'
       
    def get_expName(self):
        return self.expName

    def get_expNewFinal(self):
        return self.expNewFinal
    
    def validateName(self, name):
        return re.match(self.expName,name)      
    
    def validateNewFinal(self,name):
        return re.match(self.expNewFinal,name)

    



    


