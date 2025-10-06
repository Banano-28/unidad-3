class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def tamaño(self):
        return len(self.items)

    def mostrar(self):
        print(self.items)

def sumar_colas(cola1, cola2):
    cola_resultado = Cola()

    while not cola1.esta_vacia() and not cola2.esta_vacia():
        a = cola1.desencolar()
        b = cola2.desencolar()
        cola_resultado.encolar(a + b)
    
    return cola_resultado


if __name__ == "__main__":
    colaA = Cola()
    colaB = Cola()

    for num in [3, 4, 2, 8, 12]:
        colaA.encolar(num)

    for num in [6, 2, 9, 11, 3]:
        colaB.encolar(num)

    print("Cola A:", end=" ")
    colaA.mostrar()
    print("Cola B:", end=" ")
    colaB.mostrar()

    colaResultado = sumar_colas(colaA, colaB)

    print("Cola Resultado:", end=" ")
    colaResultado.mostrar()
