# Algoritmo que muestre la tabla de multiplicar 
# de un número introducido por teclado

num = int(input("Introduce el nº del que quieres obtener su tabla: "))
print("#######TABLA DEL ", num, "#######")
for i in range(1, 11):
    print("\t",i ,"x", num, "=", i*num)