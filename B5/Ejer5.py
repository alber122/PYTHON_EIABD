# Hacer un programa que inicialice una lista de números con valores aleatorios
# (10 valores), y posterior ordene los elementos de menor a mayor.

# Importar el random
import random
# Lista
lista_numeros = []
# Agregar números aleatorios
for i in range (1, 11):
    # Agregar los números aleatorios a la lista
    lista_numeros.append(random.randint(1,100))

# Ordenar de menos a mayor
print(sorted(lista_numeros))


