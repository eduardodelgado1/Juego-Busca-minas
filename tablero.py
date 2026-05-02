from pieza import Pieza
import random

class Tablero:
    def __init__(self, tamanio, dificultad):
        self.tamanio = tamanio
        self.dificultad = dificultad
        self.tablero = []
        
        for fila in range(tamanio[0]):
            fila = []
            for columna in range(tamanio[1]):
                tiene_bomba = random.random() < dificultad
                pieza = Pieza(tiene_bomba)
                fila.append(pieza)
            self.tablero.append(fila)
      
      # Getter y setter para encapsular el acceso a los atributos 
    def obtener_tablero(self):
        return self.tablero
    
    def obtener_tamanio(self):
        return self.tamanio