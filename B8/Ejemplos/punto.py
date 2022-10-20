# Se importa la librería con funciones matemáticas
# para los cálculos posteriores
import math

# Creación de la clase punto con sus atributos (x, y)
# y sus métodos
class Punto():
    # Método constructor, por defecto construye el punto (0,0)
    # Se ejecuta cada vez que se crea un objeto Punto
    # self hace referencia al propio objeto
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    
    # Método para mostrar el objeto
    def mostrar(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    # Devuelve la distancia de un punto a otro
    # Corresponde a la hipotenusa del triángulo rectángulo
    # que forman los dos puntos, es decir, la distancia sería
    # la diagonal que va del punto1 al punto2
    def distancia(self, otro):
        dx = self.x - otro.x
        dy = self.y - otro.y
        return math.sqrt(dx**2 + dy**2)

# Llamadas a la clase Punto
punto1=Punto()
punto2=Punto(4,5)
print("El punto 1 es", punto1.mostrar())
print("El punto 2 es", punto2.mostrar())
print(punto1.distancia(punto2))