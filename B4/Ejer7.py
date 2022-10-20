# Pide una cadena y dos caracteres por teclado (valida que sea un carácter),
# sustituye la aparición del primer carácter en la cadena por el segundo carácter.

# Pedir cadena
cadena=str(input("Escribe una cadena: "))
# Primer caracter
carac1=str(input("Dime el primer caracter: "))
# Segundo caracter
carac2=str(input("Dime el segundo caracter: "))

# Sustitución
# Comprobación de que es un caracter
if len(carac1)==1 and len(carac2)==1:
    print(cadena.replace(carac1,carac2))