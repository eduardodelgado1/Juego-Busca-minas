import pygame
 

class GestorEventos:
    def __init__(self, juego):
        self._juego = juego

    def manejar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:

                return False
            elif (
                evento.type == pygame.MOUSEBUTTONDOWN
                and not self._juego.obtener_tablero().informar_perdio()
                and not self._juego.obtener_tablero().informar_gano()
            ):
                click_derecho = evento.button == 3
                self._juego.manejar_click(evento.pos, click_derecho)
        return True
              