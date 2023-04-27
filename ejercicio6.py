import random

# Definición de la clase Carta
class Carta:
    def __init__(self, numero, palo):
        self.numero = numero
        self.palo = palo

# Generar la pila de cartas aleatoriamente
mazo = []
for numero in range(1, 13):
    for palo in ['espada', 'basto', 'copa', 'oro']:
        carta = Carta(numero, palo)
        mazo.append(carta)
random.shuffle(mazo)

# Crear las pilas correspondientes a cada palo
espada = []
basto = []
copa = []
oro = []

# Separar la pila de cartas en las pilas correspondientes a cada palo
while mazo:
    carta = mazo.pop()
    if carta.palo == 'espada':
        espada.append(carta)
    elif carta.palo == 'basto':
        basto.append(carta)
    elif carta.palo == 'copa':
        copa.append(carta)
    else:
        oro.append(carta)
        