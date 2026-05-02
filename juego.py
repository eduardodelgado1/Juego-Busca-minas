import pygame
import tkinter as tk
from tkinter import messagebox

from gestor_eventos import GestorEventos
from tablero import Tablero
from randerizador import Randerizador
from gestor_recursos import GestorRecursos


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
        self.gestor_recursos = GestorRecursos(self._tamanio_pieza)
        self._imagenes = self.gestor_recursos.cargar_imagen()
        self._gestor_eventos = GestorEventos(self)
        self._randerizador = Randerizador(self, self._pantalla, self._tamanio_pieza,self._imagenes)

        pygame.display.set_caption("Busca Minas")
        imagen_icono = pygame.image.load("images/icono.png")
        pygame.display.set_icon(imagen_icono)

    def ejecutar(self):
        ejecutando = True
        while ejecutando:
            ejecutando = self._gestor_eventos.manejar_eventos()
            if (not self._tablero.informar_perdio() or self._tablero.informar_gano()):
                self._randerizador.dibujar()
            else:
                self._randerizador.dibujar()  # Redibujar el tablero para mostrar las bombas
                pygame.display.flip()
                self.mostrar_mensaje_fin_juego(self._tablero.informar_gano())
                ejecutando = False
            pygame.display.flip()

    def obtener_tablero(self):
        return self._tablero


# Manejar los click del usuario en una celda especifica del tablero
    def manejar_click(self, posicion, bandera):        
        indice = tuple(int(pos //tamanio) for pos, tamanio in zip(posicion, self._tamanio_pieza))[::-1]
        self._tablero.manejar_click(self._tablero.obtener_pieza(indice), bandera)

    def mostrar_mensaje_fin_juego(self, gano):
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal
        mensaje = "¡Felicidades, has ganado!" if gano else "¡Has hecho clic en una bomba! Perdistes."
        messagebox.showinfo(mensaje, icon="warning")
        root.destroy()
     



        