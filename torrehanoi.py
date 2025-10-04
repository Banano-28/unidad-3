class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            return None

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            return None

    def mostrar(self):
        return self.items

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino):
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")
        mostrar_torres()
    else:
       
        hanoi(n-1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar)

        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de {nombre_origen} a {nombre_destino}")
        mostrar_torres()

        hanoi(n-1, auxiliar, origen, destino, nombre_auxiliar, nombre_origen, nombre_destino)

def mostrar_torres():
    print("Torre A:", torre_A.mostrar())
    print("Torre B:", torre_B.mostrar())
    print("Torre C:", torre_C.mostrar())
    print("-"*30)

torre_A = Pila()
torre_B = Pila()
torre_C = Pila()

torre_A.apilar(3)
torre_A.apilar(2)
torre_A.apilar(1)

print("Estado inicial:")
mostrar_torres()

print("\nResolviendo Torres de Hanoi con 3 discos:\n")
hanoi(3, torre_A, torre_B, torre_C, "A", "B", "C")
