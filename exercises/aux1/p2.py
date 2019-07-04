__author__ = "F. Giovanni Sanguineti"
__email__ = "franco.sanguineti@ug.uchile.cl"

import numpy as np

from aux1.p1 import Pokemon

# Exercise a

array_a = np.zeros(11, dtype=int)
array_a[0] = 5
array_a[10] = 5
print("Exercise a array : ", array_a, "\n")

# Exercise b

array_b = np.arange(5, 14).reshape(3, 3)
print(array_b, "\n")

# Exercise c

array_c = np.arange(32, 68)  # size: 36
print("Exercise c array : ", array_c)
array_c_inverted = np.ones(36, dtype=int)  # creates an array with 36 ones
for number in range(36):
    array_c_inverted[35 - number] = array_c[number]
print("Inverted Exercise c array : ", array_c_inverted)
print("Size of Inverted Exercise c array: ", array_c.shape)
reshaped_Exercise_c_array = array_c_inverted.reshape(6, 6)
print(reshaped_Exercise_c_array)
print("Size of Inverted Exercise c array: ", reshaped_Exercise_c_array.shape, "\n")

# Exercise d

array_d = np.empty(5, dtype='U20')
array_d[0] = "Hola amig@"
array_d[4] = "Adiós amig@"
print(array_d, "\n")

# Exercise e

array_e = np.empty(15, dtype=float)
array_e[0] = 3.3
for x in range(1, 15):
    array_e[x] = array_e[x - 1] + 0.3
print(array_e, "\n")

# Exercise f

charizard = Pokemon("Charizard", 47, 6)
gyarados = Pokemon("Gyarados", 113, 130)
evee = Pokemon("Evee", 45, 133)
array_f = np.array([charizard, gyarados, evee], dtype=Pokemon)

for pokemon in array_f:
    print(pokemon.name)
print("\n")

