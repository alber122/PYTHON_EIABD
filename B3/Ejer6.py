# Escribir un programa que imprima todos los números pares entre dos números
# que se le pidan al usuario.

# Pedir numeros
# Primer numero
num1=int(input("Dime el primer número: "))
# Segundo numero
num2=int(input("Dime el Segundo número: "))

# For para sacar los pares
for var in range(num1,num2):
    if var % 2 == 0:
        print(var,"",end="")