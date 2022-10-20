# Programa que declare una lista y la vaya llenando de números hasta que
# introduzcamos un número negativo. Entonces se debe imprimir el vector (sólo los
# elementos introducidos).

# Declaro una variable para guardar la lista
lista=[]
# Pedir agregar carácteres a la lista
aniadir=int(input("Añade caracter: "))
while aniadir>0:
    # Añadir caracter
    lista.append(aniadir)
    aniadir=int(input("Añade caracter: "))

# Mostar la lista
print(lista)