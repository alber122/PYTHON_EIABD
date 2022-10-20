# Escribe un programa que diga si un número introducido
# por teclado es o no primo. Un número primo es aquel que 
# sólo es divisible entre él mismo y la unidad.  

# Variable bandera
primo = True
num = int(input("Introduce el nº para saber si es primo o no: "))
# No se divide ni entre 1 ni entre él mismo, pues esos sabemos
# que son divisores
for i in range(2, num):
    if num % i == 0:
        # En cuanto se encuentre un divisor sale del bucle
        primo = False
        break

if primo:
    print("El nº introducido es primo")
else:
    print("El nº introducido no es primo")
