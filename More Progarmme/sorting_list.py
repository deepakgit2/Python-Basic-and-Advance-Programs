# Implementation of selection sort

# Unsorted array
arr = [39, 37, 35, 36, 35, 36, 47, 44, 32, 39, 40, 31, 36, 33, 40]

a_n = []
def fn(arr):
    k = arr[0]
    d = 0
    for i in range(len(arr)):
        if arr[i] < k:
            k = arr[i]
            d = i
    return d
for i in range(len(arr)):
    a_n += [arr[fn(arr)]]
    del arr[fn(arr)]
print a_n