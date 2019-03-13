def mergeSort(a):
    if len(a) > 1:
        b = a[:int(len(a)/2)].copy()
        c = a[int(len(a)/2):].copy()
        mergeSort(b)
        mergeSort(c)
        merge(b, c, a)


def merge(b, c, a):
    i = j = k = 0
    while i < len(b) and j < len(c):
        if b[i] <= c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
        k += 1
    if i == len(b):
        for x in c[j:]:
            a[k] = x
            k += 1
    else:
        for x in b[i:]:
            a[k] = x
            k += 1