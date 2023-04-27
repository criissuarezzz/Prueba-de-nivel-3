class Pedido:
    def __init__(self, solicitante, multiverso, descripcion):
        self.solicitante = solicitante
        self.multiverso = multiverso
        self.descripcion = descripcion
        self.siguiente = None

class Cola:
    def prioridad(pedido):
        if Pedido.solicitante == "Gran Conquistador" or Pedido.multiverso == "616" or "El que permanece" in Pedido.descripcion:
            return 3
        elif Pedido.solicitante == "Khan que todo lo sabe" or "Carnicero de Dioses" in Pedido.descripcion or Pedido.multiverso == "838":
            return 2
        else:
            return 1

    def atender_pedido(pedido):
        p= Cola.prioridad(pedido)
        nuevo_nodo=Pedido(Pedido.solicitante, Pedido.multiverso, Pedido.descripcion)
        if not cola_prioridad:
            cola_prioridad.append(nuevo_nodo)