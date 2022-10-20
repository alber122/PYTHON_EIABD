# Crear un programa de ordenador para gestionar los resultados de la quiniela de fútbol.
# Para ello vamos a utilizar dos tablas:
# Equipos: Que es una tabla de cadenas donde guardamos en cada columna el nombre de 
# los equipos de cada partido. En la quiniela se indican 15 partidos.
# Resultados: Es una tabla de enteros donde se indica el resultado. También tiene dos 
# columnas, en la primera se guarda el número de goles del equipo que está guardado en la primera columna
#  de la tabla anterior, y en la segunda los goles del otro equipo. 
# El programa ira pidiendo los nombres de los equipos de cada partido y el resultado del partido, a continuación se imprimirá la quiniela de esa jornada.
# ¿Qué modificación habría que hacer en las tablas para guardar todos los resultados de todas las jornadas de la temporada?

# Variables para el numero de equipos
num_equipos = int(input("¿Cuántos equipos hay?: "))
equipos = []
resultados = []
# For para las listas, y que no sean mas de los equipos ya nombrados
for indice in range(0,num_equipos):
	# Variable de partido
	partido = []
	# Ir agregando los equipos en 1 y 2
	partido.append(input("Introduce el nombre del equipo 1 del partido %d:" % (indice+1)))
	partido.append(input("Introduce el nombre del equipo 2 del partido %d:" % (indice+1)))
	equipos.append(partido)
	# Varibale de goles
	goles = []
	# Acumular los goles en ambos equipos
	goles.append(int(input("Introduce los goles metidos por el equipo %s:" % (partido[0]))))
	goles.append(int(input("Introduce los goles metidos por el equipo %s:" % (partido[1]))))
	resultados.append(goles)

# Dejar todo más bonito para saber donde empieza la quiniela
print("Empieza la quiniela")
print("===================")

# Junto ambas listas para ir sumando goles dependiendo de los que se hayan puesto anteriormente
for partido,goles in zip(equipos,resultados):
	print(partido[0],"-",partido[1],":",end="")
	if goles[0] > goles[1]:
		print("-> 1")
	else:
		if goles[0] < goles[1]:
			print("-> 2")
		else:
			print("-> X")
