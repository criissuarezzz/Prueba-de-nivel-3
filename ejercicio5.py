#Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea- toria– que resuelva las siguientes actividades:
#realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
#determinar si un número está cargado en el árbol o no;
#eliminar tres valores del árbol;
#determinar la altura del subárbol izquierdo y del subárbol derecho;
#determinar la cantidad de ocurrencias de un elemento en el árbol;
#contar cuántos números pares e impares hay en el árbol
#implementar TDA

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar(valor, self.raiz)
    
    def _insertar(self, valor, nodo):
        if valor < nodo.valor:
            if nodo.izquierda:
                self._insertar(valor, nodo.izquierda)
            else:
                nodo.izquierda = NodoArbol(valor)
        else:
            if nodo.derecha:
                self._insertar(valor, nodo.derecha)
            else:
                nodo.derecha = NodoArbol(valor)
    
    def barrido_preorden(self):
        self._barrido_preorden(self.raiz)
    
    def _barrido_preorden(self, nodo):
        if nodo:
            print(nodo.valor)
            self._barrido_preorden(nodo.izquierda)
            self._barrido_preorden(nodo.derecha)
    
    def barrido_inorden(self):
        self._barrido_inorden(self.raiz)
    
    def _barrido_inorden(self, nodo):
        if nodo:
            self._barrido_inorden(nodo.izquierda)
            print(nodo.valor)
            self._barrido_inorden(nodo.derecha)
    
    def barrido_postorden(self):
        self._barrido_postorden(self.raiz)
    
    def _barrido_postorden(self, nodo):
        if nodo:
            self._barrido_postorden(nodo.izquierda)
            self._barrido_postorden(nodo.derecha)
            print(nodo.valor)
    
    def barrido_por_nivel(self):
        if not self.raiz:
            return
        
        cola = [self.raiz]
        
        while len(cola) > 0:
            nodo = cola.pop(0)
            print(nodo.valor)
            
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)
    
    def buscar(self, valor):
        return self._buscar(valor, self.raiz)
    
    def _buscar(self, valor, nodo):
        if not nodo:
            return False
        elif nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar(valor, nodo.izquierda)
        else:
            return self._buscar(valor, nodo.derecha)
    
    def eliminar(self, valor):
        self.raiz = self._eliminar(valor, self.raiz)
    
    def _eliminar(self, valor, nodo):
        if not nodo:
            return None
        elif valor < nodo.valor:
            nodo.izquierda = self._eliminar(valor, nodo.izquierda)
        elif valor > nodo.valor:
            nodo.derecha = self._eliminar(valor, nodo.derecha)
        else:
            if not nodo.izquierda:
                return nodo.derecha
            elif not nodo.derecha:
                return nodo.izquierda
            else:
                nodo.valor = self._min_valor(nodo.derecha)
                nodo.derecha = self._eliminar(nodo.valor, nodo.derecha)
        return nodo

    def _min_valor(self, nodo):
        while nodo.izquierda:
            nodo = nodo.izquierda
        return nodo.valor
    
    def altura(self):
        return self._altura(self.raiz)
    
    def _altura(self, nodo):
        if not nodo:
            return 0
        else:
            return 1 + max(self._altura(nodo.izquierda), self._altura(nodo.derecha))
        
    def altura_subarbol_izquierdo(self):
        return self._altura_subarbol_izquierdo(self.raiz)
    
    def _altura_subarbol_izquierdo(self, nodo):
        if not nodo:
            return 0
        else:
            return 1 + self._altura_subarbol_izquierdo(nodo.izquierda)
        
    def altura_subarbol_derecho(self):
        return self._altura_subarbol_derecho(self.raiz)
    
    def _altura_subarbol_derecho(self, nodo):
        if not nodo:
            return 0
        else:
            return 1 + self._altura_subarbol_derecho(nodo.derecha)
        
    def ocurrencias(self, valor):
        return self._ocurrencias(valor, self.raiz)
    
    def _ocurrencias(self, valor, nodo):
        if not nodo:
            return 0
        elif nodo.valor == valor:
            return 1 + self._ocurrencias(valor, nodo.izquierda) + self._ocurrencias(valor, nodo.derecha)
        elif valor < nodo.valor:
            return self._ocurrencias(valor, nodo.izquierda)
        else:
            return self._ocurrencias(valor, nodo.derecha)
        
    def contar_pares_impares(self):
        return self._contar_pares_impares(self.raiz)
    
    def _contar_pares_impares(self, nodo):
        if not nodo:
            return (0, 0)
        elif nodo.valor % 2 == 0:
            pares_izq, impares_izq = self._contar_pares_impares(nodo.izquierda)
            pares_der, impares_der = self._contar_pares_impares(nodo.derecha)
            return (1 + pares_izq + pares_der, impares_izq + impares_der)
        else:
            pares_izq, impares_izq = self._contar_pares_impares(nodo.izquierda)
            pares_der, impares_der = self._contar_pares_impares(nodo.derecha)
            return (pares_izq + pares_der, 1 + impares_izq + impares_der)
        
    def es_avl(self):
        return self._es_avl(self.raiz)
    
    def _es_avl(self, nodo):
        if not nodo:
            return True
        elif abs(self._altura(nodo.izquierda) - self._altura(nodo.derecha)) > 1:
            return False
        else:
            return self._es_avl(nodo.izquierda) and self._es_avl(nodo.derecha)
        
if __name__=='__main__':
    import random
    for i in range(1000):
        arbol = ArbolBinario()
        for i in range(1000):
            arbol.insertar(random.randint(1, 1000))
        print('Altura:', arbol.altura())
        print('Altura subarbol izquierdo:', arbol.altura_subarbol_izquierdo())
        print('Altura subarbol derecho:', arbol.altura_subarbol_derecho())
        print('Ocurrencias del elemento:', arbol.ocurrencias(random.randint(1, 1000)))
        print('Pares e impares:', arbol.contar_pares_impares())
        eliminar=random.randint(1, 1000)
        arbol.eliminar(eliminar)
        print("Eliminar elemento:", eliminar)
        eliminar2=random.randint(1, 1000)
        arbol.eliminar(eliminar2)
        print("Eliminar elemento:", eliminar2)
        eliminar3=random.randint(1, 1000)
        arbol.eliminar(eliminar3)
        print("Eliminar elemento:", eliminar3)        
        print('Es AVL:', arbol.es_avl())
        print('----------------------')

    op=input("que elemento quieres ver si esta en el arbol?")
    print(arbol.buscar(op))
    arbol.barrido_por_nivel()
    print("Altura del arbol:",arbol.altura())
    print("Altura del subarbol izquierdo:",arbol.altura_subarbol_izquierdo())
    print("Altura del subarbol derecho:",arbol.altura_subarbol_derecho())
    print("Ocurrencias del elemento:",arbol.ocurrencias(op))
    print("Pares e impares:",arbol.contar_pares_impares())
    print("Es AVL:",arbol.es_avl())
    print("Eliminar elemento:",op)
    arbol.eliminar(op)


