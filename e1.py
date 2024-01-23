"""
Fer un programa de càlcul de temperatures del mar a fer:
Calcular per a l’any  2022: temperatura màxima, mínima i mitjana
Calcular per període 2000 a 2022: temperatura màxima, mínima i mitjana
"""

temps = ([13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14.0, 14.3, 16.0, 15.1,],
         [13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7,],
         [14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14.0, 14.3, 14.7, 15.6, 14.6,],
         [13.9, 12.5, 13.3, 13.4, 14.0, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4,],
         [13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14.0, 14.1, 14.3, 17.9, 17.7, 15.9,],
         [13.7, 12.8, 13.4, 13.9, 14.0, 14.0, 13.9, 14.0, 14.0, 14.6, 14.8, 13.3,],
         [14.1, 13.6, 12.9, 13.5, 14.0, 13.9, 14.0, 14.0, 14.2, 16.3, 16.5, 15.6,],
         [14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1,],
         [13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14.0, 14.5, 15.7, 16.5, 16.0,],
         [13.2, 12.2, 12.0, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6,],
         [13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9,],
         [13.0, 12.5, 12.5, 13.6, 13.5, 14.0, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9,],
         [12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14.0,],
         [13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14.0, 16.2, 15.9, 14.5,],
         [13.2, 13.0, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8,],
         [14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14.0, 15.5, 15.5, 13.9,],
         [12.5, 12.3, 12.1, 12.9, 13.1, 13.4, 13.2, 13.2, 14.0, 15.5, 17.3, 15.8,],
         [13.3, 12.3, 12.3, 12.9, 13.4, 13.3, 13.3, 13.4, 13.9, 15.2, 17.1, 14.4,],
         [13.5, 12.7, 12.3, 12.6, 13.2, 13.1, 13.3, 13.6, 14.9, 15.3, 15.4, 14.6,],
         [13.6, 12.2, 12.5, 12.8, 14.7, 13.5, 13.6, 13.7, 14.2, 15.9, 15.3, 15.0,],
         [13.2, 12.4, 12.9, 13.4, 13.7, 13.6, 14.4, 13.8, 14.3, 14.8, 15.3, 14.2,],
         [13.8, 13.0, 12.6, 13.6, 13.5, 13.4, 14.0, 14.0, 14.2, 15.3, 16.8, 14.0,],
         [12.7, 12.4, 12.6, 12.4, 13.0, 13.6, 13.3, 13.6, 13.5, 15.9, 15.3, 14.9])

temps_mitjana = [14.0, 14.1, 14.2, 14.1, 14.4, 14.9, 14.4, 14.4, 14.1, 14.5, 14.7, 14.8,
                 14.1, 14.6, 14.9, 14.7, 14.1, 14.8, 14.7, 14.7, 14.9, 14.8, 14.0, 14.6]

maxima2022 = 0
minima2022 = 100
any2022 = temps[0]
tempsuma2022 = 0

for n in any2022:
    if maxima2022 < n:
        maxima2022 = n
    if minima2022 > n:
        minima2022 = n
    tempsuma2022 += n

temps_mitjana2022 = round(tempsuma2022 / len(any2022), 1)

print("- Any 2022:\n   - Màxima:", maxima2022, "\n   - Mínima:", minima2022, "\n   - Mitjana:", temps_mitjana2022)

maxima2000 = 0
minima2000 = 100
tempsuma = 0

for f in range(len(temps)):
    for i in temps[f]:
        if maxima2000 < i:
            maxima2000 = i
        if minima2000 > i:
            minima2000 = i
        tempsuma += i

temps_mitjana2000 = round(tempsuma/len(temps[0]*len(temps)), 1)

print("\n- Període 2000 a 2022:\n   - Màxima:", maxima2000, "\n   - Mínima:", minima2000,
      "\n   - Mitjana:", temps_mitjana2000)
