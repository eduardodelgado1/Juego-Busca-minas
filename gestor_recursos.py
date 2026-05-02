import pygame
import os

class GestorRecursos:
    def __init__(self, tamaño_pieza):
        self._cache_imagenes = {}
        self._tamaño_pieza = tamaño_pieza

    def cargar_imagen(self, carpeta="images"):

        for nombre_archivo in os.listdir(carpeta):

            if not nombre_archivo.endswith((".png", ".jpg", ".jpeg")):
                continue

            ruta_completa = os.path.join(carpeta, nombre_archivo)

            imagen = pygame.image.load(ruta_completa)

            imagen_acomodada = pygame.transform.scale(
                imagen,
                self._tamaño_pieza
            )

            self._cache_imagenes[
                nombre_archivo.split('.')[0]
            ] = imagen_acomodada

        return self._cache_imagenes

    def obtener_imagen(self, nombre):
        return self._cache_imagenes.get(nombre)