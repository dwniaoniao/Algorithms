#!/usr/bin/python3
def insertionSort(a):
    for i in range(1, len(a)):
        temp = a[i]
        print(temp)
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -= 1
            print(a[j])
        a[j+1] = temp
        print(a)
