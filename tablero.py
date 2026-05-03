from pieza import Pieza
import random


class Tablero:
    """
    Representa el tablero principal del juego.

    Responsabilidades:
    - Generar las casillas
    - Distribuir bombas aleatoriamente
    - Gestionar clicks del usuario
    - Calcular vecinos
    - Detectar victoria o derrota
    """

    def __init__(self, tamanio, dificultad):

        # Configuración del tablero
        self.tamanio = tamanio
        self.dificultad = dificultad

        # Matriz principal del tablero
        self.tablero = []

        # =========================
        # GENERAR TABLERO
        # =========================
        # Crear una matriz de objetos Pieza
        # y asignar bombas aleatoriamente
        for fila in range(tamanio[0]):

            fila = []

            for columna in range(tamanio[1]):

                # Determinar si la casilla tendrá bomba
                tiene_bomba = random.random() < dificultad

                # Crear pieza
                pieza = Pieza(tiene_bomba)

                fila.append(pieza)

            self.tablero.append(fila)

        # Asignar vecinos a cada pieza
        self._obtener_vecinos()

        # Calcular cantidad de bombas vecinas
        self._establecer_bombas_alrededor()

        # Estados del juego
        self._perdio = False
        self._gano = False

    # =========================
    # GETTERS
    # =========================

    def obtener_tablero(self):
        """
        Retorna la matriz completa del tablero.
        """

        return self.tablero

    def obtener_tamanio(self):
        """
        Retorna el tamaño configurado del tablero.
        """

        return self.tamanio

    # =========================
    # LOGICA DE CLICK
    # =========================

    def manejar_click(self, pieza, bandera):
        """
        Procesa la interacción del jugador
        sobre una casilla.

        Parámetros:
        - pieza: objeto Pieza seleccionado
        - bandera: True si fue click derecho
        """

        # =========================
        # MARCAR BANDERA
        # =========================
        if bandera:

            pieza.alternar_marcada()

            return

        # =========================
        # EVITAR CLICKS INVALIDOS
        # =========================
        if (
            pieza.fue_clickeada()
            or pieza.informar_marcada()
        ):
            return

        # Revelar casilla
        pieza.clickear()

        # =========================
        # REVELADO RECURSIVO
        # =========================
        # Si la casilla no tiene bombas vecinas,
        # revelar automáticamente sus vecinos
        if pieza.obtener_cantidad_bombas_vecinos() == 0:

            for vecino in pieza.obtener_vecinos():

                self.manejar_click(
                    vecino,
                    False
                )

        # =========================
        # DETECTAR DERROTA
        # =========================
        if pieza.informar_tiene_bomba():

            self._perdio = True

        else:
            # Verificar si el jugador ganó
            self._gano = self.verificar_gano()

    # =========================
    # ACCESO A PIEZAS
    # =========================

    def obtener_pieza(self, indice):
        """
        Retorna una pieza específica
        según su posición en la matriz.

        Parámetro:
        - indice: tupla (fila, columna)
        """

        return self.tablero[indice[0]][indice[1]]

    # =========================
    # VECINOS
    # =========================

    def _obtener_vecinos(self):
        """
        Recorre el tablero y asigna
        las piezas vecinas de cada casilla.
        """

        for fila in range(len(self.tablero)):

            for columna in range(len(self.tablero[0])):

                pieza = self.tablero[fila][columna]

                vecinos = []

                self.agregar_lista_vecinos(
                    vecinos,
                    fila,
                    columna
                )

                pieza.establecer_vecinos(vecinos)

    def agregar_lista_vecinos(
        self,
        vecinos,
        fila,
        columna
    ):
        """
        Agrega las piezas vecinas válidas
        a una lista de vecinos.

        Evita:
        - salirse del tablero
        - agregarse a sí misma
        """

        for f in range(fila - 1, fila + 2):

            for c in range(columna - 1, columna + 2):

                # Ignorar la pieza actual
                if f == fila and c == columna:
                    continue

                # Evitar índices fuera del tablero
                if (
                    f < 0
                    or f >= self.tamanio[0]
                    or c < 0
                    or c >= self.tamanio[1]
                ):
                    continue

                vecinos.append(self.tablero[f][c])

    # =========================
    # BOMBAS ALREDEDOR
    # =========================

    def _establecer_bombas_alrededor(self):
        """
        Calcula cuántas bombas vecinas
        tiene cada pieza del tablero.
        """

        for fila in self.tablero:

            for pieza in fila:

                pieza.calcular_cantidad_bombas_vecinos()

    # =========================
    # ESTADO DEL JUEGO
    # =========================

    def informar_perdio(self):
        """
        Retorna True si el jugador perdió.
        """

        return self._perdio

    def informar_gano(self):
        """
        Retorna True si el jugador ganó.
        """

        return self._gano

    # =========================
    # VERIFICAR VICTORIA
    # =========================

    def verificar_gano(self):
        """
        Verifica si todas las casillas
        seguras fueron descubiertas.

        El jugador gana cuando:
        - todas las casillas SIN bomba
          fueron clickeadas
        """

        for fila in self.tablero:

            for pieza in fila:

                if (
                    not pieza.informar_tiene_bomba()
                    and not pieza.fue_clickeada()
                ):
                    return False

        self._gano = True

        return True