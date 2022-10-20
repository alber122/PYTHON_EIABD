# Introducir una cadena de caracteres e indicar si es un palíndromo. Una
# palabra palíndroma es aquella que se lee igual adelante que atrás.

# Pedir cadena de caracteres
cadena=str(input("Escrbie una cadena y te digo si es palíndromo: "))

# localizar el inicio
# Si cadena es igual a la cadena invertida, es palindroma, si n. no
if cadena==cadena[::-1]:
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")