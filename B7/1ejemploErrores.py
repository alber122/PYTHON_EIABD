# Ejemplo de control de excepciones en Python
while True:
    try:
        x = int(input("Introduce un número: "))
        print(100/x)
        break
    except ValueError:
        print ("Solo se permiten números enteros")
    except ZeroDivisionError:
        print("No se puede dividir por cero")
    else:
        print("Se ha producido otro error")
    finally:
        print("Siempre se ejecuta esta instrucción\ntanto si entra en try como en except")