# Hacer un programa que muestre un cronometro, indicando las horas, minutos
# y segundos.

# Fases del cronometro
from os import system
import sys
from time import sleep
from turtle import clear
# Horas
horas=0
# Minutos
minutos=0
# Segundos
segundos=0

while horas<=23:
    horas += 1
    while minutos<=59:
        minutos += 1
        while segundos<=59:
            segundos += 1
            clear
            print(horas,":",minutos,":",segundos)
            sleep(1)