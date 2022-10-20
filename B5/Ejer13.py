# De una empresa de transporte se quiere guardar el nombre de los
# conductores que tiene, y los kilómetros que conducen cada día de la semana.
# Para guardar esta información se van a utilizar dos arreglos:
#   Nombre: Lista para guardar los nombres de los conductores.
#   kms: Tabla para guardar los kilómetros que realizan cada día de la semana.
# Se quiere generar una nueva lista (“total_kms”) con los kilómetros totales que realiza cada
# conductor.
# Al finalizar se muestra la lista con los nombres de conductores y los kilómetros que ha
# realizado.

# Variable para ir guardando los días de la semana
dias_semana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

# Variable para kms y nombre de empleados
nombre_cond = []
kms = []

# While para ir pidiendo número de conductores totales de la empresa
# y que se almacenen para poder comparar luego
while True:
    num = int(input("¿Cuántos conductores totales hay?: "))
    if num > 0:
        break

# Se hace for, para que se vayan almacenando nombres de los conductores
# en la lista "nombre_cond" dependiendo de la cantidad total de la empresa
for conductores in range(0,num):
    nombre_cond.append(input("Dime el nombre de un conductor: "))
    # Calcular los kms realizar cada día
    # Variable para almacenar los kilometros cada dia
    kms_dias = []
    # For puesto que hay 7 días, y que se almacenen en la lista anterior 
    # y esos mismos, se sumen en la varibale "kms"
    for dias in range(0,7):
        kms_dias.append(input("¿Cuántos kms ha realizado este dia?"))
    kms.append(kms_dias)

# Crear la varibale "total_kms" para poder sumar todos los kilometros de cada
# conductor entre los diferentes dias de la semana
total_kms = []
# For para que se vayan sumando y guardando los resultados en la lista
for kms_s in kms:
    total_kms.append(sum(kms_s))

# Mostrar los resultados de cada conductor con sus kilometros totales
# Se ha el zip para poder mostrar ambas tablas
for nombre_c, t_km in zip(nombre_cond,total_kms):
    print("El conductor",nombre_c,"ha recorrido un total de: ",t_km)
