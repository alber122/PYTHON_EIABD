# Clase Alumn@ que hereda el nombre, edad y dni de la clase Persona ya creada

from persona import Persona
class Alumno(Persona):
    # Constructor. Utiliza super para implementar la herencia
    def __init__(self, nombre, edad, dni, modulo, nota):
        # Se usa el constructor de la clase Persona con super
        super().__init__(nombre, edad, dni)
        self.modulo = modulo
        self.nota = nota

    # Nuevos Getters
    @property
    def modulo (self):
        return self.__modulo

    @property
    def nota (self):
        return self.__nota

    # Nuevos Setters
    @modulo.setter
    def modulo(self, modulo):
        self.__modulo = modulo

    @nota.setter
    def nota(self, nota):
        if nota < 0 or nota > 10:
            self.__nota = 0.0
            print("La nota no puede ser negativa ni mayor de un 10!!")
        else:
            self.__nota = nota

    # Método que en función de la nota numérica del alumno 
    # indica si ha aprobado o no
    def esta_aprobado (self):
        if self.nota >= 5:
            print ("Enhorabuena al alumn@ " + super().mostrar() + " ha APROBADO!!") 
        else:
            print ("Lo siento pero alumn@ " + super().mostrar() + " ha SUSPENDIDO!!") 

    # Método para mostrar todos los datos del alumn@
    def mostrar (self):
        # Se muestran los atributos de Persona seguidos del los que se han añadido nuevos
        return super().mostrar() + " == MÓDULO:" + self.modulo + " == NOTA:" + str(self.nota)