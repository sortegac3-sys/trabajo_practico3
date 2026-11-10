from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)

# ------------------------- funciones de apoyo -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")

def leer_texto(mensaje):
    """Pide un texto y no deja continuar si queda vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto != "":
            return texto
        print("  No puede estar vacío.")

def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)

def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]

def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")

# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                       # 1. LEER
            if pila.apilar(pasajero):                        # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope")       # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            pasajero = pila.desapilar()                      # LLAMAR
            if pasajero is None:                             # MOSTRAR
                print("  ⚠ La pila está vacía: no hay nada que desapilar")
            else:
                print(f"  ✓ Salió: {pasajero.nombre}")
                nuevo_tope = pila.ver_tope()
                if nuevo_tope is None:
                    print("  La pila quedó vacía")
                else:
                    print(f"  Nuevo tope: {nuevo_tope.nombre}")
        elif op == "4":
            tope = pila.ver_tope()                           # LLAMAR
            if tope is None:                                 # MOSTRAR
                print("  ⚠ La pila está vacía")
            else:
                print(f"  Tope: {tope.nombre} ({tope.numero})")
        elif op == "5":
            numero = leer_entero("  N.º a buscar: ")         # LEER
            posicion = pila.buscar(numero)                   # LLAMAR
            if posicion == -1:                               # MOSTRAR
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {pila.datos[posicion].nombre}")
                print(f"  (revisó {pila.recorrido})")
        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")      # LEER
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            modificado = pila.modificar(numero, destino, asiento)   # LLAMAR
            if modificado is None:                           # MOSTRAR
                print("  No existe")
            else:
                print("  ✓ Modificado:")
                print(f"  {modificado}")
        elif op == "7":
            numero = leer_entero("  N.º a eliminar: ")       # LEER
            eliminado = pila.eliminar_por_numero(numero)     # LLAMAR
            if eliminado is None:                            # MOSTRAR
                print("  No existe")
            else:
                print(f"  ✓ Eliminado: {eliminado.nombre}")
        elif op == "8":
            copia = pila.copiar()                            # LLAMAR
            print("  ✓ Copia de la pila:")                   # MOSTRAR
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  La pila está vacía")
            else:
                print("  La pila no está vacía")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if pila.apilar(p):
                    cargados = cargados + 1
            print(f"  ✓ Datos de prueba apilados: {cargados}")
        elif op == "0":
            break
        else:
            print("  Opción no válida")

# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()                       # 1. LEER
            if cola.encolar(pasajero):                       # 2. LLAMAR
                print("  ✓ Encolado: está al final")         # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            pasajero = cola.desencolar()                     # LLAMAR
            if pasajero is None:                             # MOSTRAR
                print("  ⚠ La cola está vacía: no hay nadie que desencolar")
            else:
                print(f"  ✓ Salió: {pasajero.nombre}")
                nuevo_frente = cola.ver_frente()
                if nuevo_frente is None:
                    print("  La cola quedó vacía")
                else:
                    print(f"  Nuevo frente: {nuevo_frente.nombre}")
        elif op == "4":
            frente = cola.ver_frente()                       # LLAMAR
            if frente is None:                               # MOSTRAR
                print("  ⚠ La cola está vacía")
            else:
                print(f"  Frente: {frente.nombre} ({frente.numero})")
        elif op == "5":
            numero = leer_entero("  N.º a buscar: ")         # LEER
            posicion = cola.buscar(numero)                   # LLAMAR
            if posicion == -1:                               # MOSTRAR
                print("  No existe")
            else:
                print(f"  Encontrado en [{posicion}]: {cola.datos[posicion].nombre}")
                print(f"  (revisó {cola.recorrido})")
        elif op == "6":
            numero = leer_entero("  N.º a modificar: ")      # LEER
            destino = leer_texto("  Nuevo destino: ")
            asiento = leer_texto("  Nuevo asiento: ").upper()
            modificado = cola.modificar(numero, destino, asiento)   # LLAMAR
            if modificado is None:                           # MOSTRAR
                print("  No existe")
            else:
                print("  ✓ Modificado:")
                print(f"  {modificado}")
        elif op == "7":
            numero = leer_entero("  N.º a eliminar: ")       # LEER
            eliminado = cola.eliminar_por_numero(numero)     # LLAMAR
            if eliminado is None:                            # MOSTRAR
                print("  No existe")
            else:
                print(f"  ✓ Eliminado: {eliminado.nombre}")
        elif op == "8":
            copia = cola.copiar()                            # LLAMAR
            print("  ✓ Copia de la cola:")                  # MOSTRAR
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  La cola está vacía")
            else:
                print("  La cola no está vacía")
        elif op == "C":
            cargados = 0
            for p in datos_prueba():
                if cola.encolar(p):
                    cargados = cargados + 1
            print(f"  ✓ Datos de prueba encolados: {cargados}")
        elif op == "0":
            break
        else:
            print("  Opción no válida")

# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nPrograma interrumpido.")
