import math
# Importa la clase puntoGetSet para implementar la herencia,
# es decir, para hacer uso de los atributos y métodos que ya
# tiene esta clase
from puntoGetSet import PuntoGetSet

# Esta clase añade una tercera dimensión al punto original
class Punto3d(PuntoGetSet):
    # Constructor. Solo añade la coordenada z, pues la x e y la hereda
    def __init__(self,x=0,y=0,z=0):
        super().__init__(x,y)
        self.z=z

    # Método Get para la coordenada z. Pues para x e y lo hereda
    @property
    def z(self):
        print("Obteniendo valor de z...")
        return self.__z
    
    # Método Set para la coordenada z. Pues para x e y lo hereda
    @z.setter
    def z(self,z):
        print("Dando valor a z...")
        self.__z=z

    # Muestra las coordenadas del punto. Utiliza el método mostrar del 
    # punto con 2 dimensiones y añade la 3º dimensión, la z
    def mostrar(self):
        return super().mostrar()+","+str(self.__z)
    
        # Se cambia el cálculo de la distancia, pues ahora hay que añadir
        # el cuadrado de la coordenada z
        # CUIDADO CON EL SANGRADO, PUES AL NO USAR SUPER TIENE QUE ESTAR TABULADO 
        # RESPECTO A INIT
        def distancia(self,otro):
            dx = self.__x - otro.__x
            dy = self.__y - otro.__y
            dz = self.__z - otro.__z            
            return math.sqrt(dx*dx + dy*dy + dz*dz) 
        
# Programa principal
punto1=Punto3d()
print(type(punto1))
print ("La X del punto 1 es",punto1.x)
print ("La Y del punto 1 es",punto1.y)
print ("La Z del punto 1 es",punto1.z)
print()
print("El punto 1 es",punto1.mostrar())
print()
punto2=Punto3d(4,5,3)
print("El punto 2 es",punto2.mostrar())
print()
print(punto1.distancia(punto2))
print()
punto1.x=10
print ("Ahora la X del punto 1 es",punto1.x)