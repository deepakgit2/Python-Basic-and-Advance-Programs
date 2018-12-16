# Implementation of insertion sort

# Unsorted array
arr = [39, 37, 35, 36, 35, 36, 47, 44, 32, 39, 40, 31, 36, 33, 40]

def inserstion(j,arr=[]):
    for i in range(j):
        if arr[j]<arr[i]:
            r=arr[j]
            for k in range(j,i,-1):
                arr[k]=arr[k-1]
            arr[i]=r
    return arr
for l in range(1,len(arr)):
    inserstion(l,arr)

print 'Sorted list:',arr
