# Una persona se encuentra en el kilómetro 70 de una carretera, otra se
# encuentra en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
# Realizar un programa para determinar en qué kilómetro de esa carretera se encontrarán.

# Variable que dice el km donde se encuentra el coche 1
coche1=70
# Variable que dice el km donde se encuentra el coche 2
coche2=150
# Mientras el km del 1 no es igual que el km del segundo
# se le suma uno al coche 1, y se le resta 1 al coche 2,
# de tal forma que cuando su km coincida lo diga
while coche1!=coche2:
    coche1 += 1
    coche2 -= 1
print("Ambos coches se han encontrado en el km: ",coche2)