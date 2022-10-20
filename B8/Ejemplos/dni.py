# Clase Dni para guardar el nº del dni en una cadena de 9
# caracteres (8 dígitos y una letra)
# Tiene 2 atributos nº y letra, pero la letra se obtiene 
# a partir del número

class Dni():
    # Constructor, recibe como parámetro el número de dni
    def __init__(self, numero):
        self.numero = numero

    # Devuelve la letra que corresponde al nº de dni
    # Se trata de un método privado, que solo usa la clase Dni
    def __calcular_letra (self):
        letras = "TRWAGMYFPDXBNJZSQVHLCKE"
        # Se divide el nº de dni entre 23 y se obtiene el resto
        # Ese resto será la posición para obtener la letra de la cadena
        # de letras. p.e. si el resto es 7 la letra es F
        return letras[int(self.numero)%23]

    # Método getter que devuelve el nº de dni encapsulado
    @property
    def numero(self):
        return self.__numero

    # Método getter que devuelve la letra correspondiente al dni
    @property
    def letra(self):
        return self.__letra

    # Método setter que asigna valor al nº de dni. Sólo hay un setter
    # ya que la letra no se permite cambiarla, porque se calcula
    @numero.setter
    def numero (self, numero):        
        if len(numero) == 8 and numero.isdigit():
            self.__numero = numero
            self.__letra = self.__calcular_letra()
        else:
            self.__numero = "0"
            self.__letra = ""
            print("El DNI introducido es incorrecto!!")

    def mostrar(self):
        return self.numero + self.letra
    
