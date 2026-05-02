import pygame
 

class GestorEventos:
    def __init__(self, juego):
        self._juego = juego

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return False
        return True
              