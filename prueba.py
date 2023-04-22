class Node:
    def __init__(self, question, yes_node=None, no_node=None, hero=None):
        self.question = question
        self.yes_node = yes_node
        self.no_node = no_node
        self.hero = hero

class DecisionTree:
    def __init__(self, root_node):
        self.root = root_node
    
    def traverse(self, node):
        if node.hero:
            return node.hero
        print(node.question)
        answer = input().lower()
        if answer == "sí":
            return self.traverse(node.yes_node)
        elif answer == "no":
            return self.traverse(node.no_node)
        else:
            print("Respuesta inválida. Por favor, responde 'sí' o 'no'.")
            return self.traverse(node)
    
    def print_tree(self, node, level=0):
        if node:
            print("\t"*level + "- " + node.question)
            if node.hero:
                print("\t"*(level+1) + "-> " + node.hero)
            self.print_tree(node.yes_node, level+1)
            self.print_tree(node.no_node, level+1)

# Creamos los nodos
nodo7 = Node("¿Necesitas elegir rápidamente la próxima acción a tomar y moverte de un lugar a otro?", hero="Nick Fury")
nodo6 = Node("¿Necesitas infiltrarte con personas del lugar en una misión de recuperación?", hero="The Winter Soldier")
nodo5 = Node("¿Necesitas un líder para planear misiones de defensa y un genio en tecnología avanzada?", hero="Iron Man")
nodo4 = Node("¿Necesitas a alguien para comandar misiones de defensa y recuperación?", hero="Capitán América")
nodo3 = Node("¿Necesitas alguien para misiones intergalácticas en equipo?", hero="Khan")
nodo2 = Node("¿Necesitas alguien para misiones de recuperación sin ser detectado?", hero="Ant-Man")
nodo1 = Node("¿Necesitas alguien para destruir ejércitos completos?", hero="The Incredible Hulk")
raiz = Node("¿Necesitas alguien muy poderoso que pueda viajar por las distintas galaxias?", nodo3, nodo5)
nodo3.yes_node = Node("¿Necesitas a alguien muy hábil y útil para varias misiones?", nodo2, nodo4)
nodo5.yes_node = Node("¿Necesitas a alguien con un traje muy poderoso?", hero="Iron Man")
nodo4.yes_node = Node("¿Necesitas a alguien con ética incorruptible?", hero="Capitán América")

# Creamos el árbol
arbol_decision = DecisionTree(raiz)

# Imprimimos el árbol por pantalla
arbol_decision.print_tree(raiz)

# Realizamos una prueba de la función traverse()
print("\nEl superhéroe ideal para esta misión es: " + arbol_decision.traverse(raiz))
