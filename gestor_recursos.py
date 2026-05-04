import os
from pathlib import Path

import pygame

# Raíz del proyecto: permite ejecutar el juego desde cualquier directorio de trabajo
PROJECT_ROOT = Path(__file__).resolve().parent
IMAGES_DIR = PROJECT_ROOT / "images"


class GestorRecursos:
    def __init__(self, tamaño_pieza):
        self._cache_imagenes = {}
        self._tamaño_pieza = tamaño_pieza

    def cargar_imagen(self, carpeta=None):

        carpeta = Path(carpeta) if carpeta else IMAGES_DIR

        for nombre_archivo in os.listdir(carpeta):

            if not nombre_archivo.endswith((".png", ".jpg", ".jpeg")):
                continue

            ruta_completa = carpeta / nombre_archivo

            imagen = pygame.image.load(ruta_completa)
            if pygame.display.get_surface() is not None:
                imagen = imagen.convert_alpha()

            imagen_acomodada = pygame.transform.scale(
                imagen,
                self._tamaño_pieza
            )

            self._cache_imagenes[
                nombre_archivo.split(".")[0]
            ] = imagen_acomodada

        return self._cache_imagenes

    def obtener_imagen(self, nombre):
        return self._cache_imagenes.get(nombre)