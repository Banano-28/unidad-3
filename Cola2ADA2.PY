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

def sistema_colas():

    servicios = {
        1: Cola(),  
        2: Cola(), 
        3: Cola()   
    }

    contador_turnos = {1: 0, 2: 0, 3: 0}

    print("=== SISTEMA DE COLAS DE SERVICIO ===")
    print("Comandos:")
    print("  C <número_servicio>  -> llega un cliente (ejemplo: C1)")
    print("  A <número_servicio>  -> atender cliente (ejemplo: A2)")
    print("  S  -> salir del sistema\n")

    while True:
        comando = input("Ingrese comando: ").upper().strip()

        if comando == "S":
            print("Saliendo del sistema...")
            break

        elif comando.startswith("C"):
            try:
                servicio = int(comando[1])
                if servicio in servicios:
                    contador_turnos[servicio] += 1
                    turno = contador_turnos[servicio]
                    servicios[servicio].encolar(turno)
                    print(f"Cliente agregado al servicio {servicio} con turno número {turno}.")
                else:
                    print(" Servicio no válido.")
            except:
                print(" Formato incorrecto. Usa por ejemplo: C1 o C2.")

        elif comando.startswith("A"):
            try:
                servicio = int(comando[1])
                if servicio in servicios:
                    turno = servicios[servicio].desencolar()
                    if turno is not None:
                        print(f" Atendiendo al cliente con turno {turno} del servicio {servicio}.")
                    else:
                        print(f"No hay clientes esperando en la cola del servicio {servicio}.")
                else:
                    print(" Servicio no válido.")
            except:
                print(" Formato incorrecto. Usa por ejemplo: A1 o A2.")

        else:
            print(" Comando no reconocido. Usa C<n>, A<n> o S.")


if __name__ == "__main__":
    sistema_colas()
