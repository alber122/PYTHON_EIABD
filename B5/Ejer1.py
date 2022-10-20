# Realizar un programa que inicialice una lista con 10 valores aleatorios
# (del 1 al 10) y posteriormente muestre en pantalla cada elemento 
# de la lista junto con su cuadrado y su cubo

import random
lista_numeros = []
# 1er recorrido para rellenar la lista
for i in range (1, 11):
    lista_numeros.append(random.randint(1,10))

# 2º recorrido para mostrar el resultado
for i in lista_numeros:
    print(i, "\t", i ** 2, "\t", i ** 3)