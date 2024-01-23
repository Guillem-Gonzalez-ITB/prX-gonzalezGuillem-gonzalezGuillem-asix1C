"""
Guillem González Rodríguez
ASIXc 1C
23/1/2024


Programa que generi una llista de 100 nombres aleatoris entre 1 i 50.
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars.
"""

import random
length = 100
sumaparells = 0
sumaimparells = 0
llista_nums = []

for n in range(length):
    randomnum = random.randint(1, 50)
    llista_nums.append(randomnum)
    if n % 2 == 0:
        sumaparells += randomnum
    else:
        sumaimparells += randomnum

print("\n", llista_nums, "\nParells:", sumaparells/(length/2), "\nImparells:", sumaimparells/(length/2))
