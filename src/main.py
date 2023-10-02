from .expresion import Expresion

expresion = Expresion()

flag = False

while flag==False:
    name = input("Ingresa tu nombre: ")
    flag = expresion.verificar(name)    




