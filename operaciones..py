class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        try:
            result= self.num1 + self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")

    def resta(self):
        try:
            result= self.num1 - self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")

            