# Realizar un programa que comprueba si una cadena leída
# por teclado comienza por una subcadena introducida por teclado

cad = input("Introduce una cadena: ")
subcad = input("Introduce una cadena: ")
if cad.startswith (subcad):
    print ("La cadena comienza por la subcadena")
else:
    print ("La cadena no comienza por la subcadena")
