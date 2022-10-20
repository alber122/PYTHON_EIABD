# Función “calcularMaxMin” que recibe una lista con valores numéricos
# y devuelve el valor máximo y el mínimo. Crea un programa que pida 
# números por teclado y muestre el máximo y el mínimo, 
# utilizando la función anterior

# importar la función randint para generar valores aleatorios
from random import randint

# Entrada: lista de valores
# Salida: tupla con 2 valores, máximo y mínino
def calcularMaxMin(lista):    
    return (max(lista), min(lista))    

# Código con la llamada a la función
lista = []

# Se rellena la lista con valores aleatorios
for i in range(20):
    lista.append(randint(1, 101))

# Control de errores
try:
    # Se imprime la lista completa
    print(lista)

    # Llamada a la función que devuelve dos valores y se imprimen el máx y el mín
    if (len(lista) != 0):
        vMax, vMin = calcularMaxMin(lista)
        print("El valor máximo de la lista es: ", vMax)
        print("El valor mínimo de la lista es: ", vMin)
    else: 
        print("La lista está vacía")

except ValueError:
    print(error)