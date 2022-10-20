# Algoritmo que pida números hasta que se introduzca un cero. 
# Debe imprimir la suma y la media de todos los números introducidos

# Variable acumulador
suma = 0
media = 0
# Variable para contar la cantidad de números
contador = 0

# Bucle while que simula el bucle repetir que no existe en Python
while True:
    num = int(input("Introduce un nº (0 para salir): "))
    suma += num    
    if num != 0:
        contador += 1
    else:
        break    

print("La suma de los " ,contador, " números introducidos es: " ,suma)

# Si no se han introducido números no se puede hallar la media
if contador > 0:
    # Se halla la media
    media = suma / contador
    print("La media de los " ,contador, "números introducidos es: " ,media)
else:
    print("No se puede hallar la media porque no se han introducido números")
