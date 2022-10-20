# Si tenemos una cadena con un nombre y apellidos, realizar un programa que
# muestre las iniciales en mayúsculas.

# pedir nombre y apellidos
# Nombre
nombre=str(input("Dime un nombre: "))
# Apellidos
apellido1=str(input("Dime tu primer apellido: "))
apellido2=str(input("Dime tu segundo apellido: "))

# coge el caracter 0, es decir la primera letra
n=nombre[0]
a1=apellido1[0]
a2=apellido2[0]
# Devuelve el caracter en mayúscula
print(n.upper(),",",a1.upper(),",",a2.upper())
