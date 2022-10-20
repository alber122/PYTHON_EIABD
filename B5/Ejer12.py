# Diseñar el algoritmo correspondiente a un programa, que:
# Crea una tabla bidimensional de longitud 5x5 y nombre „diagonal‟.
# Carga la tabla de forma que los componentes pertenecientes a la diagonal de la
# matriz tomen el valor 1 y el resto el valor 0.
# Muestra el contenido de la tabla en pantalla

# Defino diagonal
fila_m = []
filas = 5
columnas = 15
for indice_fila in range(0,filas):
	fila = []
	for indice_col in range(0,columnas): 
		# Una vez aparezca en la columna, que inicialice
		if indice_fila == 0 or indice_fila == filas -1 or indice_col == 0 or indice_col == columnas -1:
			fila.append(1)
		# Si no se cumple nada de lo anterior que se inicialice en 0
		else:
			fila.append(0)
	fila_m.append(fila)
# Mostrar la tabla con las diagolanes
for fila in fila_m:
	for elemento in fila:
		print(elemento," ",end="")
	print()
