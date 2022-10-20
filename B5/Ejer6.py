# Crea un programa que pida un número de mes al usuario (por ejemplo, el 4) y
# diga cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para
# simplificarlo vamos a suponer que febrero tiene 28 días.# 

# Pedir número del mes
mes=int(input("Dime el número de un mes: "))

# Variables de listas
listanombre = ["","Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
listadias = ["",31,28,31,30,31,30,31,31,30,31,30,31]

# Variables donde se almacenan los datos a dar
nombre=listanombre[mes]
dias=listadias[mes]

# Mostrar el resultado
print("El número,",mes,"es",nombre,"y tiene",dias)

