# Realizar un programa que compruebe si una cadena contiene una subcadena.
# Las dos cadenas se introducen por teclado

cad = input("Introduce una cadena: ")
subcad = input("Introduce la subcadena a buscar: ")

if cad.find(subcad) > -1:
    print("Búsqueda con método find(). La cadena contine la subcadena buscada")
else:
    print("Búsqueda con método find(). La cadena no contine la subcadena buscada")

# Una 2ª solución es usar el operador in
if subcad in cad:
    print("Búsqueda con operador in. La cadena contine la subcadena buscada")
else:
    print("Búsqueda con operador in. La cadena no contine la subcadena buscada")
