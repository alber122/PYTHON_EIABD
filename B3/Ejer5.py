# Algoritmo que pida caracteres e imprima „VOCAL‟ si son vocales y „NO VOCAL‟
# en caso contrario, el programa termina cuando se introduce un espacio.

# Pedir caracter
caracter=str(input("Dime algun caracter: "))

# While
while caracter!=" ":
    caracter=str(input("Dime algun caracter: "))
    for v in caracter:
        if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
            print("VOCAL")
        else:
            print("NO VOCAL")
        if v==" ":
            print("Se cierra el juego")
            break
        