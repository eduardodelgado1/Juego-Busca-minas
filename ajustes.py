import pygame
import sys

# =========================
# COLORES
# =========================
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

ROJO = (255, 0, 0)

VERDE_OSCURO = (34, 139, 34)
VERDE_CLARO = (144, 238, 144)

# =========================
# DIMENSIONES VENTANA
# =========================
ANCHO_VENTANA = 400
ALTO_VENTANA = 350

# =========================
# SOMBRA BOTON
# =========================
SOMBRA_DESPLAZA = 4

# =========================
# INICIALIZAR PYGAME
# =========================
pygame.init()
pygame.font.init()


# =========================
# BOTON
# =========================
def dibujar_boton(pantalla, texto, boton):

    # sombra
    sombra_boton = pygame.Rect(
        boton.x + SOMBRA_DESPLAZA,
        boton.y + SOMBRA_DESPLAZA,
        boton.width,
        boton.height
    )

    pygame.draw.rect(
        pantalla,
        VERDE_OSCURO,
        sombra_boton,
        border_radius=12
    )

    # boton principal
    pygame.draw.rect(
        pantalla,
        VERDE_CLARO,
        boton,
        border_radius=12
    )

    # texto
    fuente = pygame.font.SysFont(None, 36)

    superficie_texto = fuente.render(
        texto,
        True,
        NEGRO
    )

    pantalla.blit(
        superficie_texto,
        (
            boton.x + (boton.width - superficie_texto.get_width()) // 2,
            boton.y + (boton.height - superficie_texto.get_height()) // 2
        )
    )


# =========================
# DESLIZADOR
# =========================
class Deslizable:

    def __init__(self, x, y, ancho, val_min, val_max, valor_inicial):

        self.x = x
        self.y = y

        self.ancho = ancho

        self.val_min = val_min
        self.val_max = val_max

        self.valor = valor_inicial

        self.rectangulo = pygame.Rect(
            self.x,
            self.y,
            self.ancho,
            20
        )

        posicion_inicial = (
            (self.valor - self.val_min)
            / (self.val_max - self.val_min)
        ) * self.ancho

        self.manija = pygame.Rect(
            self.x + posicion_inicial - 10,
            self.y - 5,
            20,
            30
        )

    def dibujar(self, pantalla):

        pygame.draw.line(
            pantalla,
            NEGRO,
            (self.x, self.y + 10),
            (self.x + self.ancho, self.y + 10),
            2
        )

        pygame.draw.rect(
            pantalla,
            ROJO,
            self.manija,
            border_radius=5
        )

    def mover_manija(self, pos):

        if self.rectangulo.collidepoint(pos):

            nueva_x = max(
                self.x,
                min(
                    pos[0] - self.manija.width // 2,
                    self.x + self.ancho - self.manija.width
                )
            )

            self.manija.x = nueva_x

            porcentaje = (
                (self.manija.x - self.x)
                / (self.ancho - self.manija.width)
            )

            self.valor = (
                self.val_min
                + porcentaje * (self.val_max - self.val_min)
            )

    def obtener_valor(self):

        # tamaño tablero
        if isinstance(self.val_min, int):
            return round(self.valor)

        # dificultad
        return round(self.valor, 2)


# =========================
# PANTALLA INICIO
# =========================
def pantalla_inicio():

    pantalla = pygame.display.set_mode(
        (ANCHO_VENTANA, ALTO_VENTANA)
    )

    pygame.display.set_caption("Busca Minas")

    imagen_icono = pygame.image.load("images/icono.png")
    pygame.display.set_icon(imagen_icono)

    fuente = pygame.font.SysFont(None, 48)
    fuente_chica = pygame.font.SysFont(None, 30)

    # sliders
    tamanio_deslizador = Deslizable(
        50,
        100,
        300,
        5,
        20,
        10
    )

    dificultad_deslizador = Deslizable(
        50,
        200,
        300,
        0.1,
        0.5,
        0.2
    )

    # boton inicio
    boton_inicio = pygame.Rect(
        ANCHO_VENTANA // 2 - 100,
        280,
        200,
        40
    )

    ejecutando = True

    while ejecutando:

        pantalla.fill(BLANCO)

        # titulo
        texto_titulo = fuente.render(
            "Busca Minas",
            True,
            NEGRO
        )

        pantalla.blit(
            texto_titulo,
            (
                ANCHO_VENTANA // 2
                - texto_titulo.get_width() // 2,
                20
            )
        )

        # sliders
        tamanio_deslizador.dibujar(pantalla)
        dificultad_deslizador.dibujar(pantalla)

        # etiquetas
        etiqueta_tamanio = fuente_chica.render(
            f"Tamaño: {tamanio_deslizador.obtener_valor()} x {tamanio_deslizador.obtener_valor()}",
            True,
            NEGRO
        )

        etiqueta_dificultad = fuente_chica.render(
            f"Dificultad: {dificultad_deslizador.obtener_valor()}",
            True,
            NEGRO
        )

        pantalla.blit(etiqueta_tamanio, (50, 140))
        pantalla.blit(etiqueta_dificultad, (50, 240))

        # boton
        dibujar_boton(
            pantalla,
            "Iniciar",
            boton_inicio
        )

        # eventos
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN:

                if boton_inicio.collidepoint(evento.pos):

                    tamanio = (
                        tamanio_deslizador.obtener_valor(),
                        tamanio_deslizador.obtener_valor()
                    )

                    dificultad = (
                        dificultad_deslizador.obtener_valor()
                    )

                    return tamanio, dificultad

                tamanio_deslizador.mover_manija(evento.pos)
                dificultad_deslizador.mover_manija(evento.pos)

            elif (
                evento.type == pygame.MOUSEMOTION
                and evento.buttons[0]
            ):

                tamanio_deslizador.mover_manija(evento.pos)
                dificultad_deslizador.mover_manija(evento.pos)

        pygame.display.flip()