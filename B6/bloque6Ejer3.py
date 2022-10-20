# Crear un programa en Python donde vamos a declarar
# un diccionario para guardar los precios de las distintas
# frutas. El programa pedirá el nombre de la fruta y la 
# cantidad que se ha vendido y nos mostrará el precio final
# de la fruta a partir de los datos guardados en el diccionario. 
# Si la fruta no existe nos dará un error. Tras cada consulta el
# programa nos preguntará si queremos hacer otra consulta

dict = {}
# Introducción de los datos en el diccionario. fruta: precio
while True:
    fruta = input("Dime la fruta: ")
    precio = float(input("Dime el precio: "))
    dict[fruta.lower()] = precio
    salir= input("Quieres introducir más frutas (s/n): ")
    if salir.lower() == "n":
        break

# Imprimir diccionario
print("=========LISTADO DE FRUTAS Y PRECIOS=========")
print("=============================================")
for clave, valor in dict.items():
    print (clave,"\t-->precio: ", valor, "€/kg")

# Pedir la cantidad de cada fruta vendida
while True:
    fruta = input ("Qué fruta has vendido? ")
    if fruta.lower() not in dict:
        print("======Lo siento pero no tenemos esa fruta!!!")
    else:
        cantidad = int(input("Dime qué cantidad has vendido: "))
        print("El precio total de", fruta.lower(), "ha sido %.2f €" % (cantidad*dict[fruta.lower()]))
    salir= input("Quieres vender otra fruta (s/n): ")
    if salir.lower() == "n":
        break