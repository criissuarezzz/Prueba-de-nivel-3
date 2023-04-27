class Pedido:
    def __init__(self, solicitante, multiverso, descripcion):
        self.solicitante = solicitante
        self.multiverso = multiverso
        self.descripcion = descripcion
        self.siguiente = None

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def esta_vacia(self):
        return self.primero == None

    def agregar(self, solicitante, multiverso, descripcion):
        nuevo_pedido = Pedido(solicitante, multiverso, descripcion)
        print("El nuevo pedido es:", nuevo_pedido.solicitante, "del multiverso", nuevo_pedido.multiverso, "con la descripción:", nuevo_pedido.descripcion, "\n")
        if self.esta_vacia():
            self.primero = nuevo_pedido
            self.ultimo = nuevo_pedido
        else:
            self.ultimo.siguiente = nuevo_pedido
            self.ultimo = nuevo_pedido

    def atender(self):
        if self.esta_vacia():
            print("No hay pedidos en la cola.")
            return
        
        primer_pedido = self.primero
        
        if primer_pedido.solicitante == "Gran Conquistador" or primer_pedido.multiverso == "616" or "El que permanece" in primer_pedido.descripcion:
            self.primero = primer_pedido.siguiente
            print("Pedido atendido con máxima prioridad.")
            
        elif primer_pedido.solicitante == "Khan que todo lo sabe" or "Carnicero de Dioses" in primer_pedido.descripcion or primer_pedido.multiverso == "838":
            self.primero = primer_pedido.siguiente
            print("Pedido atendido con prioridad media.")
            
        else:
            self.primero = primer_pedido.siguiente
            print("Pedido descartado por baja prioridad.")


# Ejemplo de uso
if __name__=="__main__":
    cola_pedidos = Cola()
    cola_pedidos.agregar("Gran Conquistador", "Multiverso 42", "Necesito una estrategia para conquistar Asgard")
    cola_pedidos.atender()
    cola_pedidos.agregar("Khan que todo lo sabe", "Universo 555", "Quiero saber cuál es el secreto de los Celestiales")
    cola_pedidos.atender()
    cola_pedidos.agregar("Capitán América", "Tierra 616", "Necesito ayuda para detener al Barón Zemo")
    cola_pedidos.atender()
    cola_pedidos.agregar("Thanos", "Multiverso 838", "Quiero eliminar la mitad del universo")
    cola_pedidos.atender()
    cola_pedidos.agregar("Loki", "Multiverso 42", "Necesito escapar de los Guardianes del Tiempo")
    cola_pedidos.atender()
    cola_pedidos.atender()
