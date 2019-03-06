#!/usr/bin/python3
def bubbleSort(a):
    n = len(a)
    for i in range(0, n-1):
        for j in range(0, n-1-i):
            if a[j+1] < a[j]:
                # swap the value of a[j] and a[j+1]
                a[j], a[j+1] = a[j+1], a[j]
