import pygame

class Randerizador:
    def __init__(self, juego, pantalla, tamanio_pieza, imagenes):
        self.juego = juego
        self.pantalla = pantalla
        self.tamanio_pieza = tamanio_pieza
        self.imagenes = imagenes
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
                rec = pygame.Rect(arriba_izquierda, self.tamanio_pieza)
                imagen = self.imagenes[self.obtener_imagen(pieza)]
                self.pantalla.blit(imagen, arriba_izquierda)   
                arriba_izquierda = (arriba_izquierda[0] + self.tamanio_pieza[0], arriba_izquierda[1])
            arriba_izquierda = (0, arriba_izquierda[1] + self.tamanio_pieza[1])

    def obtener_imagen(self, pieza):
        if pieza.fue_clickeada():
            return str(pieza.obtener_cantidad_bombas_vecinos() if not pieza.informar_tiene_bomba() else "bomba-clickeada")
        return "marcada" if pieza.informar_marcada() else "bloque-vacio"