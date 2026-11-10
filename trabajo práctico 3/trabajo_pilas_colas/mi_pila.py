from pasajero import Pasajero

class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    Mismas prohibiciones que MiLista (ver la guía): solo datos[i], while,
    for i in range(), if, aux y self.cantidad.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0
        self.recorrido = ""          # texto con los pasajeros que revisó la última búsqueda

    def apilar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # MEJORA: no repetir números
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        # Solo sale el tope. No se corre nada: el cajón queda en None.
        if self.cantidad == 0:
            return None
        pasajero = self.datos[self.cantidad - 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_tope(self):
        if self.cantidad == 0:
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        # Búsqueda lineal del TOPE al FONDO. Retorna la posición o -1.
        # Va guardando en self.recorrido a quién revisó (para mostrarlo en el menú).
        self.recorrido = ""
        for i in range(self.cantidad - 1, -1, -1):
            if self.recorrido != "":
                self.recorrido = self.recorrido + " → "
            self.recorrido = self.recorrido + self.datos[i].nombre
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        # Reutiliza buscar. Nadie cambia de lugar. Retorna el pasajero o None.
        posicion = self.buscar(numero)
        if posicion == -1:
            return None
        self.datos[posicion].destino = nuevo_destino
        self.datos[posicion].asiento = nuevo_asiento
        return self.datos[posicion]

    def eliminar_por_numero(self, numero):
        # No se puede sacar del medio: se desapila hacia una pila auxiliar
        # hasta encontrarlo, se descarta, y se vuelve a apilar lo de la auxiliar.
        aux = MiPila(self.capacidad)
        eliminado = None
        while self.cantidad > 0 and eliminado is None:
            pasajero = self.desapilar()
            if pasajero.numero == numero:
                eliminado = pasajero                  # este se descarta
            else:
                aux.apilar(pasajero)
        while aux.cantidad > 0:                       # la auxiliar invierte, al devolver se endereza
            self.apilar(aux.desapilar())
        return eliminado

    def copiar(self):
        # Se apila del fondo al tope (0 -> cantidad-1) para que el tope siga siendo el mismo.
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            nueva.apilar(Pasajero(p.numero, p.nombre, p.cedula, p.edad,
                                  p.fecha_vuelo, p.destino, p.asiento))
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
