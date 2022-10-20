# Pide una cadena y un carácter por teclado 
# (valida que sea un carácter) y muestra cuantas
# veces aparece el carácter en la cadena

# Pedir cadena
cad = input("Introduce una cadena: ")

# Algoritmo, mientras sea verdad el while, se va a ejecutar,
# en caso de que deje de ser true, es decir, no funciona o dice que no,
# se termina el bucle
while True:
    car = input("Introduce un caracter: ")
    # Comprobación de que el caracter es un caracter,
    # SIEMPRE CON len(/caracter\)
    if len(car) == 1:
        break
    else:
        print ("Tienes que introducir un solo caracter")
# Con cad.count(car) te cuenta la cantidad de caracteres,
# dependiendo del que se introduzca por teclado
print("En la cadena '", cad, "'el caracter'", car, "'aparece", cad.count(car), "veces")