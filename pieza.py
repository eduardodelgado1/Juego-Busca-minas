class Pieza:
    def __init__(self, tiene_bomba):
        self.tiene_bomba = tiene_bomba
        self.clickeada = False
        self.vecinos = []
        self.cantidad_bombas_vecinos = 0
        self.marcada = False

    def clickear(self):
        self.clickeada = True

    def fue_clickeada(self):
        return self.clickeada

    def informar_tiene_bomba(self):
        return self.tiene_bomba

    def __str__(self):
        return str(self.tiene_bomba)
    
    def establecer_vecinos(self, vecinos):
        self.vecinos = vecinos

    def obtener_cantidad_bombas_vecinos(self):
        return self.cantidad_bombas_vecinos
    
    def calcular_cantidad_bombas_vecinos(self):
        num =0
        for vecino in self.vecinos:
            if vecino.informar_tiene_bomba():
                num += 1
        self.cantidad_bombas_vecinos = num
        return self.cantidad_bombas_vecinos
    
    def obtener_vecinos(self):
        return self.vecinos
    
    def informar_marcada(self):
        return self.marcada
    
    def alternar_marcada(self):
        self.marcada = not self.marcada

