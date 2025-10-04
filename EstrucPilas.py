class Pila:
    def __init__(self, capacidad):
        self.items = []       
        self.capacidad = capacidad  

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.capacidad

    def apilar(self, item):
        if self.esta_llena():
            print(f"Error: No se puede insertar '{item}'. Pila llena (desbordamiento).")
        else:
            self.items.append(item)
            print(f"Se insertó '{item}' en la pila.")
            self.mostrar_pila()

    def desapilar(self):
        if self.esta_vacia():
            print("Error: No se puede eliminar. Pila vacía (subdesbordamiento).")
            return None
        else:
            item = self.items.pop()
            print(f"Se eliminó '{item}' de la pila.")
            self.mostrar_pila()
            return item

    def mostrar_pila(self):

        print("Estado de la pila:", self.items)
        print("TOPE =", len(self.items))
        print("-" * 30)

mi_pila = Pila(8)

mi_pila.apilar("X")   
mi_pila.apilar("Y")   
mi_pila.desapilar()   
mi_pila.desapilar()  
mi_pila.desapilar()  
mi_pila.apilar("V")   
mi_pila.apilar("W")   
mi_pila.desapilar()   
mi_pila.apilar("R")  

print("Estado final de la pila:", mi_pila.items)
print("Cantidad de elementos en la pila:", len(mi_pila.items))
