from juego import Juego
from ajustes import pantalla_inicio

def main():
    # Configuración inicial del juego (tamaño y densidad de minas desde la pantalla de ajustes)
    tamanio, dificultad = pantalla_inicio()

    g = Juego(tamanio, dificultad)
    g.ejecutar()

# Comenzar el juego
if __name__ == "__main__":
    main()