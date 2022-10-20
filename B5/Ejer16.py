# Vamos a crear un programa que tenga el siguiente menú:
#  Añadir número a la lista: Me pide un número de la lista y lo añade al final de la lista.
#  Añadir número de la lista en una posición: Me pide un número y una posición, y si la
# posición existe en la lista lo añade a ella (la posición se pide a partir de 1).
#  Longitud de la lista: te muestra el número de elementos de la lista.
#  Eliminar el último número: Muestra el último número de la lista y lo borra.
#  Eliminar un número: Pide una posición, y si la posición existe en la lista lo borra de
# ella (la posición se pide a partir de 1).
#  Contar números: Te pide un número y te dice cuántas apariciones hay en la lista.
#  Posiciones de un número: Te pide un número y te dice en que posiciones está
# (contando desde 1).
#  Mostrar números: Muestra los números de la lista
#  Salir

# Crear el menú y sus opciones
lista_menu = []
while True:
    print("\n")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opcion_menu = int(input("Dime opción: "))
    if opcion_menu == 1:
        num = int(input("Dime un número: "))
        lista_menu.append(num)
        if num == 0:
            break
        else:
            num = int(input("Dime un número: "))
            lista_menu.append(num)
    elif opcion_menu == 2:
        for num in lista_menu:
            print(num,end="\n")
        num = int(input("Dime el número que quieres cambiar: "))
        posicion = int(input("Dime la posición donde lo quieres añadir: "))
        num_posi = len(lista_menu)
        if posicion > len(lista_menu):
            print("Posición incorrecta, la lista tiene un total de: ",num_posi,"posiciones")
        else:
            lista_menu.insert(posicion - 1,num)
    elif opcion_menu == 9:
        break
    else:
        print("Has seleccionado una posición incorrecta")
