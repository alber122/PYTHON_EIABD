# Realizar un algoritmo para determinar cuánto ahorrará una persona en un
# año, si al final de cada mes deposita cantidades variables de dinero; además, se quiere
# saber cuánto lleva ahorrado cada mes.

# Pedir la cantidad de dinero que ahorra cada mes
cant_mes=float(0)
# Variable donde almacenar el dinero
dinero_anio=float(0)
# Variable para la cantidad de meses del año
mes=float(1)

# Algoritmo con for
while mes<=12:
    cant_mes=float(input("¿Cuánto dinero has ahorrado en este mes?:"))
    dinero_anio=float(dinero_anio+cant_mes)
    print("Este mes",mes," has ahorrado: ",cant_mes)
    mes = mes + 1
print("En total llevas ahorrado",dinero_anio)