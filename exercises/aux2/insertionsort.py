# Problema original: Otoño 2017

import numpy as np


def insertion_sort(a):
    print(a)
    # Invariante a[i] < a[i+1] con i=0 hasta k-2
    for k in range(a.size):
        j = k
        while j > 0 and a[j] < a[j - 1]:
            t = a[j]
            a[j] = a[j - 1]
            a[j - 1] = t
            j -= 1
    print(a)


insertion_sort(np.array([5, 4, 3, 2, 1]))
