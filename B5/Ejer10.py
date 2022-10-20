# Diseñar el algoritmo correspondiente a un programa, que:
# •	Crea una tabla (lista con dos dimensiones) de 5x5 enteros.
# •	Carga la tabla con valores numéricos enteros.
# •	Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla

tabla = []
for i in range(1, 6):
    fila = []
    for j in range(1, 6):
        fila.append(int(input("Introduce el nº de la fila %d y columna %d:" % (i,j))))
    tabla.append(fila)

# Suma las filas
indice_fila = 1
for i in tabla:
    print("La suma de los elementos de la fila %d es %d" % (indice_fila, sum(i)))
    indice_fila += 1

# Suma las columnas
for j in range(1, 6):
    suma = 0
    for i in tabla:
        suma = suma + i[j-1]
    print("La suma de los elementos de la columna %d es %d" % (j, suma))