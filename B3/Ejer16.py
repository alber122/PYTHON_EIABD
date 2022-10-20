# Una empresa les paga a sus empleados con base en las horas trabajadas en
# la semana. Realice un algoritmo para determinar el sueldo semanal de N trabajadores y,
# además, calcule cuánto pagó la empresa por los N empleados.

# Pedir la cantidad de dinero que ahorra cada mes
horas_semana=float(0)
# Variable donde almacenar el dinero
horas_acumu=float(0)
# Variable para la cantidad de meses del año
sueldohora=float(input("¿Cual es el sueldo en € que se paga la hora?: "))
# Variable del total de trabajadores
totaltrabajadores=int(input("¿Cuantos trabajadores hay en total?: "))
# Variable para calcular un trabajador
empleado=1
# Algotirmo para calcular el pago total
pago_total=horas_acumu*sueldohora
# Algoritmo con for
while empleado<=totaltrabajadores:
        horas_semana=int(input("¿Cuantas horas has trabajado esta semana, empleado?: "))
        # El total de las horas que tiene 1 empleado cada semana se van cuardando
        horas_acumu=float(horas_acumu+horas_semana)
        # Calculo del costo/h por horas trabajadas
        total=horas_semana*sueldohora
        print("Esta semana, el trabajador,",empleado,"ha ganado: ",total)
        # Se va sumando uno para que se puedan hacer todos los empleados
        empleado += 1
        # Pago total a calcular entre todos los empleados
        pago_total=float(horas_acumu*sueldohora)
print("La empresa ha pagado un total de: ",pago_total,"€, por ",totaltrabajadores,"Empleados")