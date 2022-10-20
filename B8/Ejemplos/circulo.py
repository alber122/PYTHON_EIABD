# Clase círculo cuyo atributo es el radio
class Circulo():
    def __init__(self,radio):
        # Al ejecutar esta instrucción se está llamando
        # al método setter del radio
        self.radio = radio

    # Método getter para obtener el valor del radio
    # se pone el decorador @property antes de la función y el nombre
    # de la función es el mismo que el del atributo
    @property
    def radio(self):
        print("Mostrando el valor del radio a través del getter: ")
        # El radio es un atributo privado, por eso lleva __
        return self.__radio

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