#!/usr/bin/python3

import numpy as np

def quickSort(a):
    if len(a)>1:
        s = HoarePartition(a)
        quickSort(a[:s])
        quickSort(a[s+1:])

def HoarePartition(a):
    i = 0
    j = len(a)-1
    while i<j:
        while i<len(a)-1 and a[i]<=a[0]:
            i += 1
        while 0<j and a[j]>=a[0]:
            j -= 1
        a[i],a[j] = a[j],a[i]   #swap a[i], a[j]
    a[i],a[j] = a[j],a[i]   #undo the last swap
    a[0],a[j] = a[j],a[0]
    return j

a = np.random.randint(0,10000,100)
print(a)
quickSort(a)
print(a)
