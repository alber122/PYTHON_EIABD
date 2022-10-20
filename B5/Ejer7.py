# Programa que declare tres listas „lista1‟, „lista2‟ y „lista3‟ de cinco enteros cada
# uno, pida valores para „lista1‟ y „lista2‟ y calcule lista3=lista1+lista2.

# Variables para las 3 listas
# Lista 1 vacia
lista1 = []
# Lista 2 vacia
lista2 = []
# Lista 3 vacia
lista3 = []

# Bucle for, para pedir un rango de 5 numeros enteros,
# y que se almacenen en la lista 1
for num in range(1,6):
	lista1.append(int(input("Dime un número para la primera lista: ")))

# Bucle for, para pedir un rango de 5 numeros enteros,
# y que se almacenen en la lista 2
for num in range(1,6):
	lista2.append(int(input("Dime un número para la segunda lista: ")))

# Bucle for, para que los números de las demas listas,
# se amacenen en la lista 3 haciendo la suma de cada posición,
# es decir, lista1[1]=2 y lista[1]=3, lista3 = 5
for num in range(0,5):
	lista3.append(lista1[num] + lista2[num])

# Muestro los números consecutivamente sumandos
print("La suma de los numeros (lista3=lista1 + lista2) es:")
for suma in lista3:
	print(suma," ",end="")
