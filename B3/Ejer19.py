# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones
# hasta que seleccionamos la opción de “Salir”.

# Opciones de las que se van a mostrar en pantalla
def opciones():
    print("----------------------------------")
    print("----------------------------------")
    print("---------------MENÚ---------------")
    print("----------------------------------")
    print("----------------------------------")
    print("1 - Decir hola")
    print("2 - Pedir nombre y mostrarlo")
    print("3 - Hacer una suma")
    print("0 - Salir")

# Minetras sea verdd se mostrará el menu
while True:
    #Mostraría todas las opciones de la funcion opciones
    opciones()
    # Ejecutaria las funciones
    opcion = int(input())
    # Si opcion que eliges es la uno, muestra texto
    if opcion == 1:
        print("----------------------------------")
        print("Hola como estás")
        print("----------------------------------")
    # Si la opcion que se elige es la 2, pregunta y te lo muestra
    elif opcion == 2:
        print("----------------------------------")
        nombre=str(input("¿Como te llamas?: "))
        print("Buenos días",nombre)
        print("----------------------------------")
    # Si la opcion es la 3, hace la suma de dos numeros pedidos por teclado
    elif opcion == 3:
        print("----------------------------------")
        num1=int(input("Dime el primer número: "))
        num2=int(input("Dime el segundo número: "))
        print("----------------------------------")
        total=num1+num2
        print("El resultado es: ",total)
        print("----------------------------------")
    # Si la opcion es el 0, te muestra un mensaje y sale del menú
    elif opcion == 0:
        print("Has salido del menú")
        break
