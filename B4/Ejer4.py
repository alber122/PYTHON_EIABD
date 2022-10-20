# Suponiendo que hemos introducido una cadena por teclado 
# que representa una frase (palabras separadas por espacios), 
# realiza un programa que cuente cuantas palabras tiene

contador = 0
posicion = 0
cad = input("Introduce una cadena: ")
# Eliminar espacios delante y detrás
cad = cad.strip()
# Buscar espacios
posicion = cad.find(" ", posicion)
while posicion != -1:
    contador += 1
    # No tengo en cuenta los posibles espacios entre palabras
    while cad[posicion + 1] == " ":
        posicion += 1
    posicion = cad.find(" ", posicion + 1)
print("La cadena tiene", contador+1, "palabras")