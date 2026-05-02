import pygame
 

class GestorEventos:
    def __init__(self, juego):
        self._juego = juego

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:

                return False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                click_derecho = pygame.mouse.get_pressed(num_buttons=3)[2]
                self._juego.manejar_click(pygame.mouse.get_pos(), click_derecho)
        return True
              