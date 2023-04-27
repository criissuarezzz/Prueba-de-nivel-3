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
    
class Mazo:
    mazo=Pila()
    palo_espada=Pila()
    palo_basto=Pila()
    palo_oro=Pila()
    palo_copa=Pila()

    def generar_aleatoria():
        for i in range(1,13):
            for palo in ["Espada","Basto","Oro","Copa"]:
                carta=Carta(i,palo)
                Mazo.mazo.apilar(carta)
        random.shuffle(Mazo.mazo.items)

    def separar():
        while not Mazo.mazo.esta_vacia():
            carta=Mazo.mazo.desapilar()
            if carta.palo=="Espada":
                Mazo.palo_espada.apilar(carta)
            elif carta.palo=="Basto":
                Mazo.palo_basto.apilar(carta)
            elif carta.palo=="Oro":
                Mazo.palo_oro.apilar(carta)
            else:
                Mazo.palo_copa.apilar(carta)

    def ordenar():
        ordenado=Pila()
        while not Mazo.palo_espada.esta_vacia():
            carta=Mazo.palo_espada.desapilar()
            while not ordenado.esta_vacia() and ordenado.ver_tope().numero > carta.numero:
                Mazo.palo_espada.apilar(ordenado.desapilar())
            Mazo.ordenado.apilar(carta)
        while not ordenado.esta_vacia():
            Mazo.palo_espada.apilar(ordenado.desapilar())

    def imprimir():
        print("Espada: ",Mazo.palo_espada)
        print("Basto: ",Mazo.palo_basto)
        print("Oro: ",Mazo.palo_oro)
        print("Copa: ",Mazo.palo_copa)

if __name__=='__main__':
    Mazo.generar_aleatoria()
    Mazo.separar()
    Mazo.ordenar()
    Mazo.imprimir()

    