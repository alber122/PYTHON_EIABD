# Escribe un programa que pida el límite inferior y superior de un intervalo. Si el
# límite inferior es mayor que el superior lo tiene que volver a pedir.
# A continuación se van introduciendo números hasta que introduzcamos el 0. Cuando
# termine el programa dará las siguientes informaciones:
# La suma de los números que están dentro del intervalo (intervalo abierto).
# Cuantos números están fuera del intervalo.
# He informa si hemos introducido algún número igual a los límites del intervalo.

# Pedir limites
# Limite inferior
lim_inf=int(input("Dime un número como limite inferior: "))
# Limite superior
lim_sup=int(input("Dime un número como limite superior: "))

# Variable para num, puesto que está dentro de un while
num=1
# Crear variables para la suma de números dentro del intervalo
sum_inter=0
# Variable para cantidad de números fuera del intervalo
cant_fuera=0
# Variable que informa de algun número igual a los limites
# Se queda en false, hasta que alguno sea igual y se ejecute en True
igual=False

# Error en caso de que se cumpla de que el límite inferior es más grande al superior
if lim_inf>lim_sup:
    print("ERROR, no puede ser el límite inferior más grande que el superior")
# Continuar con el algoritmo hasta que se pulse el 0
while num!=0:
    num=int(input("Dime otro número (o pulsa 0 para salir): "))
    # Limite inferior mas grande que el superior
    if lim_inf>lim_sup:
        print("ERROR, no puede ser el límite inferior más grande que el superior")
        num=int(input("Dime otro número (o pulsa 0 para salir): "))
    # Números dentro del intervalo
    if num>lim_inf & num<lim_sup:
        sum_inter=sum_inter+num
    else:
        cant_fuera += 1
    # Números iguales a los limites
    if num==lim_inf or num==lim_sup:
        igual= True
        num=int(input("Dime otro número (o pulsa 0 para salir): "))
# En caso de que se introducca alguno igual, o no, que salte algun mensaje
if igual:
    print("- Número igual a alguno de los dos limites")
else:
    print("- Ningún igual a alguno de los dos limites ")

# Decir la cantidad total de unos y otros
print("- La suma de los números que están dentro son: ",sum_inter)
print("- La cantidad total de números que están fuera son: ",cant_fuera)
