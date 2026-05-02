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
        self._obtener_vecinos()
        self._establecer_bombas_alrededor()
      
      # Getter y setter para encapsular el acceso a los atributos 
    def obtener_tablero(self):
        return self.tablero
    
    def obtener_tamanio(self):
        return self.tamanio
    
    def manejar_click(self, pieza):
        if pieza.fue_clickeada():
            return 
        pieza.clickear()
        if pieza.obtener_cantidad_bombas_vecinos() == 0:
            for vecino in pieza.obtener_vecinos():
                self.manejar_click(vecino)
         

    def obtener_pieza(self, indice):
        return self.tablero[indice[0]][indice[1]]
    
    def _obtener_vecinos(self):
        for fila in range(len(self.tablero)):
            for columna in range(len(self.tablero[0])):
                pieza=self.tablero[fila][columna]
                vecinos = []
                self.agregar_lista_vecinos(vecinos, fila, columna)
                pieza.establecer_vecinos(vecinos)
               
    
    def agregar_lista_vecinos(self, vecinos, fila, columna):
            for f in range(fila - 1, fila+2):
                for c in range(columna - 1, columna+2):
                    if f == fila and c == columna:
                        continue
                    if f < 0 or f >= self.tamanio[0] or c < 0 or c >= self.tamanio[1]:
                        continue
                    vecinos.append(self.tablero[f][c])

    def _establecer_bombas_alrededor(self):
        for fila in self.tablero:
            for pieza in fila:
                pieza.calcular_cantidad_bombas_vecinos()
