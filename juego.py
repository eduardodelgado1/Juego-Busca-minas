import pygame
from gestor_eventos import GestorEventos
from tablero import Tablero
from randerizador import Randerizador

class Juego:
    def __init__(self,tamanio,dificultad):
        self.tamanio = tamanio
        self.dificultad = dificultad
        self._tablero = Tablero(tamanio, dificultad)
        pygame.init()

        self._tamanio_pieza = (40, 40)
        self._tamnio_pantalla =(self._tamanio_pieza[0] * tamanio[0], 
                                self._tamanio_pieza[1] * tamanio[1])
        self._pantalla = pygame.display.set_mode(self._tamnio_pantalla)
        self._gestor_eventos = GestorEventos(self)
        self._randerizador = Randerizador(self, self._pantalla, self._tamanio_pieza)

        pygame.display.set_caption("Busca Minas")
        imagen_icono = pygame.image.load("images/icono.png")
        pygame.display.set_icon(imagen_icono)

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            ejecutando = self._gestor_eventos.manejar_eventos()
            self._randerizador.dibujar()
            pygame.display.flip()

    def obtener_tablero(self):
        return self._tablero

        