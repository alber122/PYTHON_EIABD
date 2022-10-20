# El día juliano correspondiente a una fecha es un número entero que indica
# los días que han transcurrido desde el 1 de enero del año indicado. 
# Ejemplo: día juliano del 18 de Enero es 18
# Queremos crear un programa principal que al introducir una fecha nos diga 
# el día juliano que corresponde. Para ello podemos hacer las siguientes subrutinas:
# •	leerFecha: Nos permite leer por teclado una fecha (día, mes y año).
# •	diasDelMes: Recibe un mes y un año y nos dice los días de ese mes en ese año.
# •	esBisiesto: Recibe un año y nos dice si es bisiesto.
# •	calcularDiaJuliano: recibe una fecha y nos devuelve el día juliano

# Pide el dia, mes y año comprobando que los valores están en el rango correcto
# Entrada: ninguna
# Salida: dia, mes, año
def LeerFecha ():
    # Control de errores
    try:
        # Se obliga a que los valores sean válidos, para el día, mes y año
        while True:
            dia = int(input("Introduce un dia: "))
            if (dia > 0) and (dia < 32):
                break

        while True:
            mes = int(input("Introduce un mes: "))
            if (mes > 0) and (mes < 13):
                break
                
        while True:
            anio = int(input("Introduce un año: "))
            if (anio > 0):
                    break     
        # Devuelve los tres valores       
        return dia, mes, anio
    except ValueError:
        print("Se ha producido un error ", error)

# Calcula si un año es bisiesto o no
# Entrada: año
# Salida: True si es bisiesto, False si no lo es
def esBisiesto(anio):
    if ((anio % 4) == 0 and not (anio % 100) == 0) or ((anio % 400) == 0):
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto

# Función que devuelve los días que tiene el mes indicado
# Entrada: mes, anio
# Salida: número de días del mes indicado
def diasDelMes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        diasM = 31
    elif mes in [4, 6, 9, 11]:
        diasM = 30
    elif mes == 2:
        # Se llama a la función que devuelve si el año es bisiesto o no
        if esBisiesto(anio):
            diasM = 29
        else:
            diasM = 28
    return diasM

# Calcula el día juliano
# Entrada: dia, mes, año
# Salida: dia juliano    
def calcularDiaJuliano(dia, mes, anio):
    # Contador de días
    diaJ = 0
    for mes in range (1, mes):
        # Se llama a la función que calcula los días que tiene el mes indicado en cada iteración
        diaJ += diasDelMes(mes, anio)
    diaJ += dia
    return diaJ

# Código con las llamadas a las funciones definidas
dia, mes, anio = LeerFecha()
print("Día Juliano: ", calcularDiaJuliano(dia, mes, anio))
