# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que
# es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad
# es opcional. Construye los siguientes métodos para la clase:
#  Un constructor, donde los datos pueden estar vacíos.
#  Los setters y getters para cada uno de los atributos. El atributo no se puede
#  modificar directamente, solo ingresando o retirando dinero.
#  mostrar(): Muestra los datos de la cuenta.
# ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
#  negativa, no se hará nada.
#  retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en
# números rojos.


# Definimos clase
from types import CellType


class Cuenta():
    # Constructor
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__cantidad = cantidad

    # Getters
    @property
    def titular(self):
        return self.__titular

    # Getter de cantidad
    @property
    def cantidad(self):
        return self.__cantidad

    # Setter
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    # Definir mostrar para que muestre la cuenta de banco
    def mostrar(self):
        return "==== CUENTA ====\n"+"Titular: "+self.titular.mostrar()+"\n - Cantidad : "+str(self.cantidad)

    
    # Si la cantidad es superior a 0
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    # Cuenta en numeros rojos
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

cuen= Cuenta("PEPE", cantidad=344)
print(cuen.mostrar())