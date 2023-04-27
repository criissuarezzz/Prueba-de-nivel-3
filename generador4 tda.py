#implementando el enunciado en tda y nodos
import random
import math

class Nodo:
    def __init__(self, valor=None, siguiente=None):
        self.valor = valor
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.largo = 0

    def agregar(self, valor):
        nuevo = Nodo(valor)
        if self.primero is None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.siguiente = nuevo
            self.ultimo = nuevo
        self.largo += 1

    def __len__(self):
        return self.largo

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            valor = self.actual.valor
            self.actual = self.actual.siguiente
            return valor
        
def leer_numero(ini, fin, mensaje):

    while True:
        try:
            numero = int(input(mensaje))
            if numero >= ini and numero <= fin:
                return numero
            else:
                print("El número debe estar entre", ini, "y", fin)
        except:
            print("Debes introducir un número")

def generador():
    numeros = leer_numero(1, 20, "¿Cuantos números quieres generar? [1-20]: ")
    modo = leer_numero(1, 3, "¿Cómo quieres redondear los números? [1]Al alza [2]A la baja [3]Normal: ")
    lista = ListaEnlazada()
    for i in range(numeros):
        numero = random.uniform(0, 100)
        if modo == 1:
            numero = math.ceil(numero)
        elif modo == 2:
            numero = math.floor(numero)
        lista.agregar(numero)
        print("Número original:", numero, "Redondeado:", lista.ultimo.valor)
    return lista

generador()
