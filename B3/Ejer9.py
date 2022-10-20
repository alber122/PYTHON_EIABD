# Escribe un programa que dados dos números, uno real (base) y un entero
# positivo (exponente), saque por pantalla el resultado de la potencia. No se puede utilizar el
# operador de potencia.

# Pedir dos números
# Base
base=float(input("Dime un número Base: "))
# exponente
expo=int(input("Dime un número entero como exponente: "))
# Resultado de la potencia
result_pot=1

# En caso de que sea 0 el expo el resultado sea 1,
for var in range(1,expo+1):
    result_pot = result_pot * base

# En caso de que sea un número negativo salte error y salga
if expo<0:
        print("Error, el número tiene que ser positivo")
        exit

print("El resultado de la potencia es: ", int(result_pot))
