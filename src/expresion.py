import re

class Expresion:

    def __init__(self):
       self.patron = r'^[A-Z][a-zA-Z]{2,}$'
       
    
    def verificar(self, name):

        if re.match(self.patron,name):
            return True
        else: 
            return False
        

    



    


