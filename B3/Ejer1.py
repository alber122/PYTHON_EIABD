# Crea una aplicación que pida un número y calcule su factorial
# (El factorial de un número es el producto de todos los enteros 
# entre 1 y el propio número y se representa por el número seguido 
# de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120)


# Variable acumulador del producto
resultadoW = 1
num = int (input("Introduce el número: "))
# Solución iterativa con bucle while
print ("SOLUCIÓN CON WHILE")
# Da igual a 1 que a 2
contador = 2
while contador <= num:
    # 1ª forma 
    resultadoW = resultadoW * contador
    contador += 1
print("El resultado usando un while de ", num, "! es: ", resultadoW)

# Solución iterativa con bucle for
print ("SOLUCIÓN CON FOR")
resultadoF = 1
for contador in range(2, num +1):
    # 2ª forma 
    resultadoF *= contador
print("El resultado usando un for de ", num, "! es: ", resultadoF)