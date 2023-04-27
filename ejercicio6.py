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
    