# Programa que pida dos números enteros al usuario y 
# diga si alguno de ellos es múltiplo del otro. 
# Crea una función EsMultiplo que reciba los dos números,
# y devuelva si el primero es múltiplo del segundo

# Se importa la función valor absoluto
from math import fabs

# Entrada: dos números
# Salida: verdadero si el 1er nº es múltiplo del 2º y falso si no lo es.
def esMultiplo(n1, n2):
    if (fabs(n1) >= fabs(n2)) and ((n1 % n2) == 0):
        esMult = True
    else:
        esMult = False
    return esMult

# Código que hace Llamada a la función
try:
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    if esMultiplo(n1, n2):
        print(n1, "es múltiplo de ", n2)
    else:
        print(n1, "no es múltiplo de ", n2)
except ValueError:
    print("Se ha producido un error al introducir los números. Pon más atención")

