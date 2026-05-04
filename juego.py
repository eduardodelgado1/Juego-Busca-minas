import pygame
import tkinter as tk
from tkinter import messagebox

# Importación de módulos internos del proyecto
from gestor_eventos import GestorEventos
from tablero import Tablero
from randerizador import Randerizador
from gestor_recursos import GestorRecursos, IMAGES_DIR


class Juego:
    """
    Clase principal del juego.

    Se encarga de:
    - Inicializar Pygame
    - Crear el tablero
    - Gestionar el ciclo principal del juego
    - Controlar eventos
    - Coordinar el renderizado
    - Detectar victoria o derrota
    """

    def __init__(self, tamanio, dificultad):

        # Configuración general del juego
        self.tamanio = tamanio
        self.dificultad = dificultad

        # Crear tablero con el tamaño y dificultad seleccionados
        self._tablero = Tablero(tamanio, dificultad)

        # Inicializar Pygame
        pygame.init()

        # Tamaño visual de cada casilla del tablero
        self._tamanio_pieza = (40, 40)

        # Calcular dimensiones totales de la ventana
        self._tamanio_pantalla = (
            self._tamanio_pieza[0] * tamanio[0],
            self._tamanio_pieza[1] * tamanio[1]
        )

        # Crear ventana principal
        self._pantalla = pygame.display.set_mode(
            self._tamanio_pantalla
        )

        # Cargar recursos gráficos del juego
        self.gestor_recursos = GestorRecursos(
            self._tamanio_pieza
        )

        # Diccionario con imágenes cacheadas
        self._imagenes = self.gestor_recursos.cargar_imagen()

        # Sistema de eventos del juego
        self._gestor_eventos = GestorEventos(self)

        # Encargado del renderizado visual
        self._randerizador = Randerizador(
            self,
            self._pantalla,
            self._tamanio_pieza,
            self._imagenes
        )

        # Configuración de ventana
        pygame.display.set_caption("Busca Minas")

        pygame.display.set_icon(
            pygame.image.load(IMAGES_DIR / "icono.png")
        )

    def ejecutar(self):
        """
        Ciclo principal del juego.

        Se ejecuta continuamente hasta que:
        - el usuario cierre la ventana
        - el jugador pierda
        - o decida salir del juego
        """

        ejecutando = True

        while ejecutando:

            # Procesar eventos de teclado y mouse
            ejecutando = self._gestor_eventos.manejar_eventos()

            partida_activa = (
                not self._tablero.informar_perdio()
                and not self._tablero.informar_gano()
            )

            if partida_activa:
                self._randerizador.dibujar()
            else:
                self._randerizador.dibujar()
                pygame.display.flip()

                if self.mostrar_mensaje_fin_juego(
                    self._tablero.informar_gano()
                ):
                    self.reiniciar_juego()
                else:
                    ejecutando = False

            # Actualizar pantalla
            pygame.display.flip()

    def obtener_tablero(self):
        """
        Retorna la instancia actual del tablero.
        """

        return self._tablero

    def manejar_click(self, posicion, bandera):
        """
        Procesa los clicks realizados por el usuario.

        Parámetros:
        - posicion: coordenadas del mouse
        - bandera: indica si fue click derecho
        """

        # Convertir posición de mouse a índice del tablero
        indice = tuple(
            int(pos // tamanio)
            for pos, tamanio in zip(
                posicion,
                self._tamanio_pieza
            )
        )[::-1]

        # Delegar lógica al tablero
        self._tablero.manejar_click(
            self._tablero.obtener_pieza(indice),
            bandera
        )

    def mostrar_mensaje_fin_juego(self, gano):
        """
        Muestra ventana emergente de victoria o derrota.

        Parámetros:
        - gano: booleano que indica si el jugador ganó

        Retorna:
        - True si el usuario quiere volver a jugar
        - False si desea salir
        """

        root = tk.Tk()

        # Ocultar ventana principal de Tkinter
        root.withdraw()

        mensaje = (
            "¡Felicidades, has ganado!"
            if gano
            else "¡Has hecho clic en una bomba! Perdiste."
        )

        respuesta = messagebox.askquestion(
            "Fin de partida",
            f"{mensaje}\n\n¿Deseas jugar de nuevo?",
            icon="warning"
        )

        root.destroy()

        return respuesta == "yes"

    def reiniciar_juego(self):
        """
        Reinicia completamente el estado del juego.
        """

        # Crear nuevo tablero
        self._tablero = Tablero(
            self.tamanio,
            self.dificultad
        )

        # Recargar imágenes
        self._imagenes = (
            self.gestor_recursos.cargar_imagen()
        )

        # Reinicializar renderizador
        self._randerizador = Randerizador(
            self,
            self._pantalla,
            self._tamanio_pieza,
            self._imagenes
        )

        # Reinicializar gestor de eventos
        self._gestor_eventos = GestorEventos(self)