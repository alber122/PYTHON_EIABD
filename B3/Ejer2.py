# Crea una aplicación que permita adivinar un número. La aplicación genera un
# número aleatorio del 1 al 100. A continuación va pidiendo números y va respondiendo si el
# número a adivinar es mayor o menor que el introducido, además de los intentos que te
# quedan (tienes 10 intentos para acertarlo). El programa termina cuando se acierta el
# número (además te dice en cuantos intentos lo has acertado), si se llega al límite de
# intentos te muestra el número que había generado.

# Generar el número aleatorio
from random import randint
random=randint(1,100)

# Preguntar por un número
num=int(input("Dime un número del 1 al 100: "))

# Contador
contador=0

print(random)

while contador!=10:
    contador += 1
    print("Has fallado, llevas --> ",contador,"/10")
    num=int(input("Dime un número del 1 al 100: "))
    if num==random:
        print("Enhorabuena, has acertado el Número con ",contador,"intentos.")
        break
    if num>random:
        print("El número correcto es menos")
    else:
        print("El número correcto es mayor")
    if contador==10:
        print("Ya no tienes mas intentos, el número correcto es: ",random)
        break
print("El juego ha terminado")