#!/usr/bin/python3

import numpy as np

def selectionSort(a):
    n = len(a)
    for i in range(0,n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        a[i],a[min] = a[min],a[i]   #swap a[i] and a[min]

a = np.random.randint(0,10000,100)
print(a)
selectionSort(a)
print(a)

