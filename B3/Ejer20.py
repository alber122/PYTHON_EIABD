# Mostrar en pantalla los N primeros número primos. Se pide por teclado la
# cantidad de números primos que queremos mostrar.

# Pedir números primos
cant=int(input("Dime la cantidad de números primos que quieres que muestre: "))

# Contador para poner todos los numeros
contador=0

# While para ir mostrando los numeros

while cant > 0:
    cant=int(input("Dime la cantidad de números primos que quieres que muestre: "))
    if cant%cant==0:
        contador=contador+1
    elif cant%1==0:
        contador=contador+1
    elif cant%2==0:
        print("No es primo")
    elif cant==0:
        break
    else:
        print("No es primo")
    if contador==2:
        print("El número es primo")
print("La cantidad de números primos es: ",contador)