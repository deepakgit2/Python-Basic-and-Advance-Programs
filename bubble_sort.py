# Implementation of bubble sort

# Unsorted array
arr = [39, 37, 35, 36, 35, 36, 47, 44, 32, 39, 40, 31, 36, 33, 40]

def sort(arr = []):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if arr[i] >= arr[j]:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
    return arr
print 'Sorted list:',sort(arr)