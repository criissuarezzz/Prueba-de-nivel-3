import random
import math

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
    lista = []
    for i in range(numeros):
        numero = random.uniform(0, 100)
        if modo == 1:
            numero = math.ceil(numero)
        elif modo == 2:
            numero = math.floor(numero)
        lista.append(numero)
        print("Número original:", numero, "Redondeado:", lista[i])
    return lista

generador()


