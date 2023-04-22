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

        # Crear nodos intermedios con preguntas
        pregunta_vuela = Nodo(pregunta="¿Puede volar?", izquierda=iron_man, derecha=hulk)
        pregunta_fuerza = Nodo(pregunta="¿Tiene mucha fuerza?", izquierda=khan, derecha=pregunta_vuela)
        pregunta_invisibilidad = Nodo(pregunta="¿Puede volverse invisible?", izquierda=ant_man, derecha=nick_fury)
        pregunta_inteligencia = Nodo(pregunta="¿Es muy inteligente?", izquierda=pregunta_fuerza, derecha=pregunta_invisibilidad)
        pregunta_lider = Nodo(pregunta="¿Es un buen líder?", izquierda=pregunta_inteligencia, derecha=thor)
        pregunta_etica = Nodo(pregunta="¿Tiene una ética incorruptible?", izquierda=capitan_america, derecha=capitana_marvel)
        pregunta_recuperacion = Nodo(pregunta="¿Es bueno en misiones de recuperación?", izquierda=winter_soldier, derecha=pregunta_lider)

       