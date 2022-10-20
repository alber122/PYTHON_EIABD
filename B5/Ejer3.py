# Se quiere realizar un programa que lea por teclado las 5 notas
# obtenidas por un alumno (comprendidas entre 0 y 10). 
# A continuación debe mostrar todas las notas, la nota media, 
# la nota más alta que ha sacado y la menor

# Se crea la lista para notas
notas = []

# Crear for con rango para las 5 notas
for i in range (1, 6):
    # Mientras sea verdad lo que está dentro del while, se ejecuta
    while True:
        nota = int(input("Introduce la nota % d:" % i))
        # Si la nota es mayor o igual a 0 o menos o igual a 10
        # y vuelve a pedir la siguiente nota
        if nota >=0 and nota <=10:
            break
    # Al final de todo, va guardando las notas
    notas.append(nota)

# Se muestran los resultados
print("Notas: ", end="")
for i in notas:
    print(i, " ", end="")
print()
print("Nota media: ", sum(notas)/len(notas))
print("Nota máxima: ", max(notas))
print("Nota mínima: ", min(notas))