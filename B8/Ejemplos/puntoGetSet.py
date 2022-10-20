import math
# Representación de un punto en el plano, los atributos son x e y
# que representan los valores de las coordenadas cartesianas.
# En este caso se han incluído getter y setter para los atributos
class PuntoGetSet(): 
    # Constructor    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    
    # Getters
    @property
    def x(self):
        print("Obteniendo valor de x...")
        return self.__x
    
    @property
    def y(self):
        print("Obteniendo valor de y...")
        return self.__y

    # Setters   
    @x.setter
    def x(self,x):
        print("Dando valor a x...")
        self.__x=x

    @y.setter
    def y(self,y):
        print("Dando valor a y...")
        self.__y=y

    # Muestra las coordenadas del punto
    def mostrar(self):
        return str(self.__x) + "," + str(self.__y)
    
    # Devuelve la distancia de un punto a otro
    # Corresponde a la hipotenusa del triángulo rectángulo
    # que forman los dos puntos, es decir, la distancia sería
    # la diagonal que va del punto1 al punto2
    def distancia(self, otro):        
        dx = self.__x - otro.__x
        dy = self.__y - otro.__y
        return math.sqrt((dx**2 + dy**2))

# Llamadas a la clase PuntoGetSet
# punto1=PuntoGetSet()
# punto2=PuntoGetSet(4,5)
# print("El punto 1 es", punto1.mostrar())
# print("El punto 2 es", punto2.mostrar())
# print("Distancia de un punto a otro:", punto1.distancia(punto2))