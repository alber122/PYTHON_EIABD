# Una empresa tiene el registro de las horas que trabaja diariamente un
# empleado durante la semana (seis días) y requiere determinar el total de éstas, así como el
# sueldo que recibirá por las horas trabajadas.

# Pedir la cantidad de dinero que ahorra cada mes
horas_dia=float(0)
# Variable donde almacenar el dinero
horas_semana=float(0)
# Variable para la cantidad de meses del año
dias_semana=float(1)
# Algoritmo con for
while dias_semana<=6:
    if horas_dia>24:
        print("No se pueden trabajar mas de 24h en un día")
        break
    else:
        horas_dia=float(input("¿Cuántas horas has trabajado hoy?"))
        horas_semana=float(horas_semana+horas_dia)
        print("Hoy, dia",dias_semana," has trabajado",horas_dia,"horas")
        dias_semana = dias_semana + 1
        # variable para denominar cuanto ha cobrado por el total de horas
        dinero_horas=float(horas_semana*6)
    
print("Esta semana has trabajado un total de: ",horas_semana,"horas")
print("Esta semana vas a cobrar",dinero_horas,"€")