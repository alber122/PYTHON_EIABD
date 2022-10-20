# Escribir por pantalla cada carácter de una cadena introducida por teclado

# Pedir cadena y que te devuelva los caracteres
cadena = str(input("Escribe alguna cadena: "))

# Recorrer la cadena y devolver los caracteres
for caracter in cadena:
    print(caracter,end="\n")