# Crea una lista e inicialízala con 5 cadenas de caracteres leídas por teclado.
# Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos
# por la pantalla

# Variables de las listas
lista1=[]
lista2=[]

# While para añadir a la lista 1 los caracteres
while len(lista1)<5:
        lista = input("Introduce 5 caracteres: ")
        lista1.append(lista)

# Almacena la lista 1 en la lista 2
lista2=lista1[:]
# Muestra la lista 2 invertida
print(lista2[::-1])
