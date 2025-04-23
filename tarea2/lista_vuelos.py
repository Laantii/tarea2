# archivo: lista_vuelos.py

class Nodo:
    def __init__(self, vuelo):
        self.vuelo = vuelo
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self._longitud = 0

    def insertar_al_frente(self, vuelo):
        nuevo = Nodo(vuelo)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo
        self._longitud += 1

    def insertar_al_final(self, vuelo):
        nuevo = Nodo(vuelo)
        if self.cola is None:
            self.cabeza = self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo
        self._longitud += 1

    def obtener_primero(self):
        return self.cabeza.vuelo if self.cabeza else None

    def obtener_ultimo(self):
        return self.cola.vuelo if self.cola else None

    def longitud(self):
        return self._longitud

    def insertar_en_posicion(self, vuelo, posicion):
        if posicion < 0 or posicion > self._longitud:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            return self.insertar_al_frente(vuelo)
        elif posicion == self._longitud:
            return self.insertar_al_final(vuelo)
        
        nuevo = Nodo(vuelo)
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        anterior = actual.anterior

        anterior.siguiente = nuevo
        nuevo.anterior = anterior
        nuevo.siguiente = actual
        actual.anterior = nuevo
        self._longitud += 1

    def extraer_de_posicion(self, posicion):
        if posicion < 0 or posicion >= self._longitud:
            raise IndexError("Posición fuera de rango")
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        
        if actual.anterior:
            actual.anterior.siguiente = actual.siguiente
        else:
            self.cabeza = actual.siguiente
        
        if actual.siguiente:
            actual.siguiente.anterior = actual.anterior
        else:
            self.cola = actual.anterior

        self._longitud -= 1
        return actual.vuelo
