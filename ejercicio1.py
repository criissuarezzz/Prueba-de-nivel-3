class Nodo:
    def __init__(self, pregunta=None, superheroe=None, izquierda=None, derecha=None):
        self.pregunta = pregunta
        self.superheroe = superheroe
        self.izquierda = izquierda
        self.derecha = derecha

class ArbolDecision:
    def __init__(self):
        # Crear nodos hoja con los superhéroes
        iron_man = Nodo(superheroe="Iron Man")
        hulk = Nodo(superheroe="Hulk")
        khan = Nodo(superheroe="Khan")
        thor = Nodo(superheroe="Thor")
        capitan_america = Nodo(superheroe="Captain América")
        capitana_marvel = Nodo(superheroe="Capitana Marvel")
        ant_man = Nodo(superheroe="Ant-Man")
        nick_fury = Nodo(superheroe="Nick Fury")
        winter_soldier = Nodo(superheroe="The Winter Soldier")
