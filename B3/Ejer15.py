# Una persona adquirió un producto para pagar en 20 meses. El primer mes
# pagó 10 €, el segundo 20 €, el tercero 40 € y así sucesivamente. Realizar un algoritmo para
# determinar cuánto debe pagar mensualmente y el total de
# lo que pagó después de los 20 meses.

# Variable donde se almacena el pago, en este caso el primero el 10
pagos=float(10)
# variable deonde se almacena el pago acumulado
pagos_total=float(0)
# variable donde se va sumando uno, por cada mes que avance
mes=float(1)

# While
while mes<=19:
    # El pago final es los pagos que ya hay, mas lo que se añadan
    pagos_total=float(pagos_total+pagos)
    # Los pagos se van multiplicando por dos cada mes
    pagos=float(pagos*2)
    # Cada mes se suma uno
    mes=float(mes+1)
print("Has pagado un total de: ",pagos_total,"€")
print("El mes",mes,"has pagado: ",pagos,"€")