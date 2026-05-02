from juego import Juego

def main():
    #Configuracion Inicial del juego
    tamanio =(10,10)
    #Dificultad relacionada con cantidad de bombas
    dificultad =0.2


    g = Juego(tamanio, dificultad)
    g.ejecutar()

# Comenzar el juego
if __name__ == "__main__":
    main()