from postres import ListaPostres

def eliminar_repetidos(lista_postres):
    actual = lista_postres.cabeza
    nombres_vistos = set()
    anterior = None

    while actual:
        if actual.nombre in nombres_vistos:
            anterior.siguiente = actual.siguiente
            print(f" Eliminado duplicado: {actual.nombre}")
        else:
            nombres_vistos.add(actual.nombre)
            anterior = actual
        actual = actual.siguiente

#Ejemplo de uso 
if __name__ == "__main__":
    lista = ListaPostres()
    lista.insertar_postre("Flan")
    lista.insertar_postre("Pastel")
    lista.insertar_postre("Flan")  
    lista.insertar_postre("Gelatina")

    lista.mostrar_postres()
    eliminar_repetidos(lista)
    lista.mostrar_postres()
