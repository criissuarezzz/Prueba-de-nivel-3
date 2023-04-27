import random

# Definición de la clase Carta
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

    def __str__(self):
        return str(self.numero) + " de " + self.palo
    
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0
    
    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items.pop()
    
    def ver_tope(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.items[-1]
    
    def tamanio(self):
        return len(self.items)
    
    def __str__(self):
        return str([str(item) for item in self.items])
    


if __name__=='__main__':
    mazo = Pila()
    palo_espada = Pila()
    palo_basto = Pila()
    palo_copa = Pila()
    palo_oro = Pila()

    # Generar el mazo de cartas de manera aleatoria
    for i in range(1, 13):
        for palo in ["espada", "basto", "copa", "oro"]:
            carta = Carta(i, palo)
            mazo.apilar(carta)
            
    random.shuffle(mazo.items)

    # Separar el mazo en cuatro pilas una por cada palo
    while not mazo.esta_vacia():
        carta = mazo.desapilar()
        if carta.palo == "espada":
            palo_espada.apilar(carta)
        elif carta.palo == "basto":
            palo_basto.apilar(carta)
        elif carta.palo == "copa":
            palo_copa.apilar(carta)
        else:
            palo_oro.apilar(carta)

    # Ordenar la pila de espadas de manera creciente por número        
    ordenado = Pila()
    while not palo_espada.esta_vacia():
        carta = palo_espada.desapilar()
        while not ordenado.esta_vacia() and ordenado.ver_tope().numero > carta.numero:
            palo_espada.apilar(ordenado.desapilar())
        ordenado.apilar(carta)
    while not ordenado.esta_vacia():
        palo_espada.apilar(ordenado.desapilar())

    # Imprimir las cuatro pilas
    print("Palo de Espada:", palo_espada)
    print("\n")
    print("Palo de Basto:", palo_basto)
    print("\n")
    print("Palo de Copa:", palo_copa)    
    print("\n")
    print("Palo de Oro:", palo_oro)    
    print("\n")
