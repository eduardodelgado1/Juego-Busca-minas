from juego import Juego
from ajustes import pantalla_inicio

def main():
    #Configuracion Inicial del juego
    tamanio, dificultad = pantalla_inicio()
    #Dificultad relacionada con cantidad de bombas
    dificultad =0.2


    g = Juego(tamanio, dificultad)
    g.ejecutar()

# Comenzar el juego
if __name__ == "__main__":
    main()