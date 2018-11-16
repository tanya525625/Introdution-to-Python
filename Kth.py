#Find the k-th smallest element in the array
import random

def get_kth(data, k):
    QSORT(data, k, data[0], data[len(data) - 1])
    return data[k - 1]


def QSORT(data, k, start, end):
    if start >= end:
        return

    i = start
    j = end
    key = data[random.randint(start, end)]

    while i <= j:
        while data[i] < key and i <= end:
            if data[i] > key and i == end:
                i = start
            i += 1
        while data[j] > key and j >= start:
            if j == start and data[j] < key:
                j = end
            j -= 1
        if i <= j:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
            i += 1
            j -= 1
            if k < i:
                QSORT(data, k, start, j)
            else:
                QSORT(data, k, i, end)


print(get_kth([0, 1, 2, 3, 4, 5], 3))
print(get_kth([1, 0, 8, 9, 7, 5], 3))
