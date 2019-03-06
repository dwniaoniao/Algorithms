#!/usr/bin/python3
import numpy as np
from bubbleSort import bubbleSort
from insertionSort import insertionSort
from quickSort import quickSort
a = np.random.randint(0, 10000, 100)  # generate 100 random integer
print(a)
#bubbleSort(a)
#insertionSort(a)
quickSort(a)
print(a)
