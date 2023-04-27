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
operacion2=Operaciones(5, 0)
operacion3=Operaciones(3, "hola") 

lista=ListaEnlazada()

resultado_suma=operacion1.suma()
resultado_resta=operacion1.resta()
resultado_producto=operacion1.producto()
resultado_division=operacion2.division()
resultado_division2=operacion3.division()

print("El resultado de la suma entre los valores 10 y 5 es: ", resultado_suma)
print("El resultado de la resta entre los valores 10 y 5 es: ", resultado_resta)
print("El resultado del producto entre los valores 10 y 5 es: ", resultado_producto)
print("El resultado de la división entre los valores 5 y 0 es: ", resultado_division)
print("El resultado de la división entre los valores 3 y 'hola' es: ", resultado_division2)

lista.agregar(operacion1)
lista.agregar(operacion2)
lista.agregar(operacion3)

