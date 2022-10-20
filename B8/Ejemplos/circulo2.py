# Clase círculo cuyos atributos son:
# centro de tipo Punto (Delegación)
# radio entero
class Circulo2():
    def __init__(self, centro, radio):
        # Al ejecutar estas instrucciones se está llamando
        # a los métodos setter
        self.centro = centro
        self.radio = radio


    # Método getter para obtener el valor del centro
    # se pone el decorador @property antes de la función y el nombre
    # de la función es el mismo que el del atributo
    @property
    def centro(self):
        print("Mostrando el valor del centro a través del getter: ")
        # El centro es un atributo privado, por eso lleva __
        return self.__centro

    # Método getter para obtener el valor del radio
    # se pone el decorador @property antes de la función y el nombre
    # de la función es el mismo que el del atributo
    @property
    def radio(self):
        print("Mostrando el valor del radio a través del getter: ")
        # El radio es un atributo privado, por eso lleva __
        return self.__radio
      
    # Método setter para poner valor al centro
    # se pone el decorador @atributo.setter
    # antes de la fución y el nombre de la función
    # es el mismo que el del atributo
    @centro.setter
    def centro(self,centro):        
            self.__centro = centro        

    # Método setter para poner valor al radio
    # se pone el decorador @atributo.setter
    # antes de la fución y el nombre de la función
    # es el mismo que el del atributo
    @radio.setter
    def radio(self,radio):
        if radio >= 0:
            print("El radio se asigna desde el setter")
            self.__radio = radio
        else:
            print("El radio debe ser positivo")
            self.__radio = 0   

    def mostrar (self):
        return "Centro:{0}-Radio:{1}".format(self.centro.mostrar(), self.radio)         