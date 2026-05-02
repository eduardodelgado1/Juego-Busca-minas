import pygame

class Randerizador:
    def __init__(self, juego, pantalla, tamanio_pieza):
        self.juego = juego
        self.pantalla = pantalla
        self.tamanio_pieza = tamanio_pieza

        ruta_imagen = "images/bloque-vacio.png"

        imagen = pygame.image.load(ruta_imagen)

        self.imagen_acomodada = pygame.transform.scale(
            imagen,
            (
                int(self.tamanio_pieza[0]),
                int(self.tamanio_pieza[1])
            )
        )

    def dibujar(self):
        arriba_izquierda = (0, 0)

        for fila in self.juego.obtener_tablero().obtener_tablero():
            for pieza in fila:

                self.pantalla.blit(
                    self.imagen_acomodada,
                    arriba_izquierda
                )

                arriba_izquierda = (
                    arriba_izquierda[0] + self.tamanio_pieza[0],
                    arriba_izquierda[1]
                )

            arriba_izquierda = (
                0,
                arriba_izquierda[1] + self.tamanio_pieza[1]
            )