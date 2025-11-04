class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class ListaIngredientes:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre):
        nuevo = NodoIngrediente(nombre)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre == nombre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.cabeza
        ingredientes = []
        while actual:
            ingredientes.append(actual.nombre)
            actual = actual.siguiente
        return ingredientes


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = ListaIngredientes()
        self.siguiente = None


class ListaPostres:
    def __init__(self):
        self.cabeza = None

    def insertar_postre(self, nombre):
        nuevo = NodoPostre(nombre)
        if not self.cabeza or nombre < self.cabeza.nombre:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente and actual.siguiente.nombre < nombre:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        print(f" Postre '{nombre}' agregado.")

    def buscar_postre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.siguiente
        return None

    def mostrar_ingredientes(self, nombre):
        postre = self.buscar_postre(nombre)
        if postre:
            print(f"\nIngredientes de '{nombre}': {postre.ingredientes.mostrar()}")
        else:
            print(f"⚠️ Postre '{nombre}' no encontrado.")

    def insertar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            postre.ingredientes.agregar(ingrediente)
            print(f" Ingrediente '{ingrediente}' agregado a '{nombre_postre}'.")
        else:
            print(f" No existe el postre '{nombre_postre}'.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        postre = self.buscar_postre(nombre_postre)
        if postre:
            if postre.ingredientes.eliminar(ingrediente):
                print(f" Ingrediente '{ingrediente}' eliminado de '{nombre_postre}'.")
            else:
                print(f" Ingrediente '{ingrediente}' no encontrado en '{nombre_postre}'.")
        else:
            print(f" No existe el postre '{nombre_postre}'.")

    def eliminar_postre(self, nombre_postre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre == nombre_postre:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f" Postre '{nombre_postre}' eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print(f" No se encontró el postre '{nombre_postre}'.")

    def mostrar_postres(self):
        print("\n Lista de postres:")
        actual = self.cabeza
        while actual:
            print(f"- {actual.nombre} ({', '.join(actual.ingredientes.mostrar())})")
            actual = actual.siguiente
