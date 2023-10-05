from pyformlang.cfg import Variable, Terminal, Production, CFG

class Gramatica:

    def __init__(self):
        # Definir variables
        self.oracion = Variable("oracion")
        self.sujeto = Variable("Sujeto")
        self.verbo = Variable("Verbo")
        self.conector = Variable("Conector")
        self.articulo = Variable("Articulo")
        self.sustantivo = Variable("Sustantivo")
        self.preposicion = Variable("Preposicion")

        # Definir términales
        self.yo = Terminal("Yo")
        self.creo = Terminal("creo")
        self.puede = Terminal("puede")
        self.mejorar = Terminal("mejorar")
        self.con = Terminal("con")
        self.que = Terminal("que")
        self.el = Terminal("el")
        self.final = Terminal("final")

        # Definir producciones
        productions = [
            Production(self.oracion, [self.sujeto, self.verbo, self.conector, self.articulo, self.sustantivo, self.verbo, self.verbo, self.preposicion]),
            Production(self.sujeto, [self.yo]),
            Production(self.verbo, [self.creo]),
            Production(self.conector, [self.que]),
            Production(self.articulo, [self.el]),
            Production(self.sustantivo, [self.final]),
            Production(self.verbo, [self.puede]),
            Production(self.verbo, [self.mejorar]),
            Production(self.preposicion, [self.con])
        ]

        # Creación del CFG
        self.glc = CFG(
            terminals={
                self.yo, self.creo, self.puede, self.mejorar, self.con, self.que, self.el, self.final
            },
            variables={
                self.oracion, self.sujeto, self.verbo, self.conector, self.articulo, self.sustantivo, self.preposicion
            },
            start_symbol=self.oracion,
            productions=productions
        )

    def validar_cadena(self, cadena):
       cadena_lista = cadena.split(" ")
       conjunto_terminales = self.glc.terminals
       lista_verificar = []
       for i in cadena_lista:
          if i=="Yo" or i=="creo" or i=="que" or i=="el" or i=="final" or i=="puede" or i=="mejorar" or i=="con":
            tmp = Terminal(i)
            lista_verificar.append(tmp)
       return self.glc.contains(lista_verificar)


