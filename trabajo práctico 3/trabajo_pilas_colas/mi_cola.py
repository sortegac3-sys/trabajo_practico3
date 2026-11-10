from pasajero import Pasajero

class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    Mismas prohibiciones que MiLista (ver la guía): solo datos[i], while,
    for i in range(), if, aux y self.cantidad.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0
        self.recorrido = ""          # texto con los pasajeros que revisó la última búsqueda

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        if self.buscar(pasajero.numero) != -1:        # MEJORA: no repetir números
            print(f"  ⚠ Ya existe un pasajero con el número {pasajero.numero}")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- recorre SIEMPRE del frente al final -------
    def desencolar(self):
        # Solo sale el frente datos[0]; todos los demás se corren un lugar a la izquierda.
        if self.cantidad == 0:
            return None
        pasajero = self.datos[0]
        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        # Búsqueda lineal del FRENTE al FINAL. Retorna la posición o -1.
        self.recorrido = ""
        for i in range(self.cantidad):
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
        # No se puede sacar del medio: la fila da UNA vuelta completa.
        # Se desencola cantidad veces; el buscado se descarta y los demás vuelven a la fila.
        total = self.cantidad
        eliminado = None
        for i in range(total):
            pasajero = self.desencolar()
            if pasajero.numero == numero:
                eliminado = pasajero                  # este no vuelve a entrar
            else:
                self.encolar(pasajero)
        return eliminado

    def copiar(self):
        # Se encola del frente al final.
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            nueva.encolar(Pasajero(p.numero, p.nombre, p.cedula, p.edad,
                                   p.fecha_vuelo, p.destino, p.asiento))
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0
