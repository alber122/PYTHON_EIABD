# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI
# El DNI se crea por DELEGACIÓN, es decir, haciendo uso de la clase Dni
# que previamente hemos creado

# Importar DNI de otro archivo ("dni")
from dni import Dni

class Persona():
    # Constructor con los atributos: nombre, edad, dni
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    # Getters de los atributos
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad
    
    @property
    def dni(self):
        return self.__dni

    # Setters de los atributos
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @edad.setter
    def edad(self, edad):
        # La edad tendrá que ser positiva
        if edad > 18:
            self.__edad = edad
            print("Es mayor de edad")
        else:
            self.__edad = edad
            print("Es menor de edad")

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    # Método para mostrar el objeto de tipo Persona con todas sus propiedades
    def mostrar(self):
        return "DNI:" + self.dni.mostrar() + " == NOMBRE:" + self.nombre + " == EDAD:" + str(self.edad) + " años"

    # Devuelve un valor lógico indicando si es mayor de edad.
    def esMayorDeEdad(self):
        return "Es menor de edad si tiene menos de 18 años\n""Es mayor de edad si tiene mas de 18 años"
    

# Crear persona
per1 = Persona("Ana", 9, Dni("73411049"))
print(per1.mostrar())
print(per1.esMayorDeEdad())
