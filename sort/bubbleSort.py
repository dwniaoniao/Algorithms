#!/usr/bin/python3
import numpy as np

def bubbleSort(a):
    n = len(a)
    for i in range(0,n-1):
        for j in range(0,n-1-i):
            if a[j+1]<a[j]:
                a[j],a[j+1] = a[j+1],a[j]   #swap the value of a[j] and a[j+1]

a = np.random.randint(0,10000,100)  #generate 100 random integer
print(a)
bubbleSort(a)
print(a)

