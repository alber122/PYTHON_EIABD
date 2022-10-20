# Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de
# números a introducir). El programa debe informar de cuantos números introducidos son
# mayores que 0, menores que 0 e iguales a 0.

# Pedir cantidad de números
cant=int(input("Dime una cantidad de números: "))

# Contadores de mayores, menores e iguales a 0
totalnum=int(0)
con_mayores=int(0)
con_menores=int(0)
con_iguales=int(0)


# Empieza el bucle con for
while True:
    num=int(input("Dime números: "))
    totalnum += 1
    print(totalnum)
    if num>0:
        con_mayores += 1
    if num<0:
        con_menores += 1
    if num==0:
        con_iguales += 1
    if cant<=totalnum:
        print("La cantidad de números mayores de 0 es: ",con_mayores)
        print("La cantidad de números menores de 0 es: ",con_menores)
        print("La cantidad de números iguales de 0 es: ",con_iguales)
        break
print("Hemos terminado")