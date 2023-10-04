import gui 
from transductor import Transductor

if __name__ == '__main__':
    gui.create_window()
    transductor = Transductor()

    cadena_entrada = "Nvk od oev lo frn rovuon ronblzddbn"
    cadena_traducida = transductor.translate(cadena_entrada)
    print(cadena_entrada)
    # Imprime la cadena traducida
    print(cadena_traducida)

    