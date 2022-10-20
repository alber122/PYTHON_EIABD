# Algoritmo que muestre la tabla de multiplicar de los números 1, 2, 3, 4 y 5

# Se usan dos bucles (for) anidados
for i in range(1, 6):
    print("#######TABLA DEL ", i, "#######")
    for j in range(1, 11):
        print("\t %d x %d = %d" % (j, i, j*i))