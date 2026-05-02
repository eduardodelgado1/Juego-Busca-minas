class Pieza:
    def __init__(self, tiene_bomba):
        self.tiene_bomba = tiene_bomba

    def movimiento_valido(self, tablero, origen, destino):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")