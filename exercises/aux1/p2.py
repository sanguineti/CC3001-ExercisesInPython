__author__ = "F. Giovanni Sanguineti"
__email__ = "franco.sanguineti@ug.uchile.cl"

import numpy as np

from p1 import Pokemon

# Exercise a

array_a = np.zeros(11, dtype=int)
array_a[0] = 5
array_a[10] = 5
print("Exercise a array : ", array_a, "\n")

# Exercise b

array_b = np.arange(5, 14).reshape(3, 3)
print(array_b, "\n")

# Exercise c
array_c = np.zeros((5, 5))
for i in range(len(array_c)):
    for j in range(len(array_c[i])):
        array_c[i][j] = 2
print(array_c)

# Exercise d

array_d = np.arange(32, 68)  # size: 36
print("Exercise d array : ", array_d)
array_d_inverted = np.ones(36, dtype=int)  # creates an array with 36 ones
for number in range(36):
    array_d_inverted[35 - number] = array_d[number]
print("Inverted Exercise d array : ", array_d_inverted)
print("Size of Inverted Exercise d array: ", array_d.size)
reshaped_Exercise_d_array = array_d_inverted.reshape(6, 6)
print(reshaped_Exercise_d_array)
print("Size of Inverted Exercise d array: ", reshaped_Exercise_d_array.shape, "\n")

# Exercise e

array_e = np.empty(5, dtype='U20')
array_e[0] = "Hola amig@"
array_e[4] = "Adiós amig@"
print(array_e, "\n")

# Exercise f

array_f = np.empty(15, dtype=float)
array_f[0] = 3.3
for x in range(1, 15):
    array_f[x] = array_f[x - 1] + 0.3
print(array_f, "\n")

# Exercise g

charizard = Pokemon("Charizard", 47, 6)
gyarados = Pokemon("Gyarados", 113, 130)
evee = Pokemon("Evee", 45, 133)
array_g = np.array([charizard, gyarados, evee], dtype=Pokemon)

for pokemon in array_g:
    print(pokemon.name)
print("\n")
