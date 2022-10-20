# Queremos guardar los nombres y las edades de los alumnos de un curso.
# Realiza un programa que introduzca el nombre y la edad de cada alumno. 
# El proceso de lectura de datos terminará cuando se introduzca como nombre un asterisco (*).
# Al finalizar se mostrará los siguientes datos:
# •	Todos los alumnos mayores de edad.
# •	Los alumnos mayores (los que tienen más edad)

# Se implementa mediante dos listas: una de nombres y otra de edad
lista_nom_alum = []
lista_edad_alum = []

# Se rellenan las listas
while True:
    nombre = input("Introduce el nombre de alumn@: ")
    if nombre == '*':
        break
    lista_nom_alum.append(nombre)
    edad = int(input("Introduce la edad de alumn@: "))    
    lista_edad_alum.append(edad)
# Se muestra la lista de todos los alumn@s
print("*****LISTADO COMPLETO DE ALUMN@S*****")
for i, j in zip(lista_nom_alum, lista_edad_alum):
    print("Alumn@:", i, "---Edad:", j)    
    
# Sólo se muestran los mayores de edad
print("*****LISTADO DE ALUMN@S MAYORES DE EDAD*****")
for i, j in zip(lista_nom_alum, lista_edad_alum):
    if j >= 18:
        print("Alumn@:", i, "---Edad:", j)

# Sólo se muestran los que tienen la edad más alta
edad_mayor = max(lista_edad_alum)
print("*****ALUMN@S MAYORES*****")
for i, j in zip(lista_nom_alum, lista_edad_alum):
    if j == edad_mayor:
        print("Alumn@:", i, "---Edad:", j)



