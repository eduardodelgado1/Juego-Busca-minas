class Pieza:
    def __init__(self, tiene_bomba):
        self.tiene_bomba = tiene_bomba
        self.clickeada = False

    def clickear(self):
        self.clickeada = True

    def fue_clickeada(self):
        return self.clickeada