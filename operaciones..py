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
    
    def producto(self):
        try:
            result= self.num1 * self.num2
            return result
        except TypeError:
            print("Error: Tipo de dato no válido")

    def division(self):
        try:
            if self.num2==0:
                raise ZeroDivisionError
            result= self.num1 / self.num2
            return result
        except ZeroDivisionError:
            print("Error: División entre cero")
        except TypeError:
            print("Error: Tipo de dato no válido")

class Nodo:
    def __init__(self, operacion, siguiente=None):
        self.operacion = operacion
        self.siguiente = siguiente
    
    def obtener_operacion(self):
        print("La operación es: ", self.operacion)

    def obtener_siguiente(self):
        return self.siguiente
    
    def asignar_siguiente(self, siguiente):
        self.siguiente = siguiente

class ListaEnlazada: 
    def __init__(self):
        self.primero=None

    def esta_vacia(self):
        return self.primero==None
    
    def agregar(self, operacion):
        nuevo_nodo=Nodo(operacion)
        nuevo_nodo.asignar_siguiente(self.primero)
        self.primero=nuevo_nodo

    def eliminar(self):
        if self.primero==None:
            print("La lista está vacía")
            return None
        nodo_eliminado=self.primero
        self.primero=self.primero.obtener_siguiente()
        return nodo_eliminado.obtener_operacion()
    


operacion1=Operaciones(10, 5)
operacion2=Operaciones(5, "hola")
operacion3=Operaciones(5, 5) 
operacion4=Operaciones(10, 0)

lista=ListaEnlazada()

resultado_suma=operacion1.suma()
resultado_resta=operacion2.resta()
resultado_producto=operacion3.producto()
resultado_division=operacion4.division()

print("{} + {} = {}".format(operacion1.num1, operacion1.num2, resultado_suma))
print("{} - {} = {}".format(operacion2.num1, operacion2.num2, resultado_resta))
print("{} * {} = {}".format(operacion3.num1, operacion3.num2, resultado_producto))
print("{} / {} = {}".format(operacion4.num1, operacion4.num2, resultado_division))




lista.agregar(operacion1)
lista.agregar(operacion2)
lista.agregar(operacion3)

