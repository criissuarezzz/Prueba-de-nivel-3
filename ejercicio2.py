# Definimos la clase Pedido
class Pedido:
    def __init__(self, nombre, multiverso, descripcion):
        self.nombre = nombre
        self.multiverso = multiverso
        self.descripcion = descripcion

# Creamos la cola de pedidos y la pila "bitácora"
cola_pedidos = []
pila_bitacora = []

# Función para agregar un nuevo pedido a la cola
def agregar_pedido(nombre, multiverso, descripcion):
    nuevo_pedido = Pedido(nombre, multiverso, descripcion)
    print("El pedido es: " + nuevo_pedido.nombre + " del" + nuevo_pedido.multiverso + " y su descripción es: " + nuevo_pedido.descripcion)
    cola_pedidos.append(nuevo_pedido)

# Función para atender el siguiente pedido en la cola
def atender_pedido():
    if len(cola_pedidos) == 0:
        print("No hay pedidos en la cola.")
        return
    
    primer_pedido = cola_pedidos[0]
    
    if primer_pedido.nombre == "Gran Conquistador" or primer_pedido.multiverso == "616" or "El que permanece" in primer_pedido.descripcion:
        pila_bitacora.append(primer_pedido)
        cola_pedidos.pop(0)
        print("Pedido atendido con máxima prioridad.")
        
    elif primer_pedido.nombre == "Khan que todo lo sabe" or "Carnicero de Dioses" in primer_pedido.descripcion or primer_pedido.multiverso == "838":
        pila_bitacora.append(primer_pedido)
        print("Pedido atendido con prioridad media.")
        
    else:
        cola_pedidos.pop(0)
        print("Pedido descartado por baja prioridad.")

# Ejemplo de uso
agregar_pedido("Gran Conquistador", "Multiverso 42", "Necesito una estrategia para conquistar Asgard")
atender_pedido()
agregar_pedido("Khan que todo lo sabe", "Universo 555", "Quiero saber cuál es el secreto de los Celestiales")
atender_pedido()
agregar_pedido("Capitán América", "Tierra 616", "Necesito ayuda para detener al Barón Zemo")
atender_pedido()
agregar_pedido("Thanos", "Multiverso 838", "Quiero eliminar la mitad del universo")
atender_pedido()
agregar_pedido("Loki", "Multiverso 42", "Necesito escapar de los Guardianes del Tiempo")
atender_pedido()
atender_pedido()

