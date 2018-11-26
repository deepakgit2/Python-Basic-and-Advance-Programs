# Implementation of recursive quick sort

# Unsorted array
arr = [39, 37, 35, 36, 35, 36, 47, 44, 32, 39, 40, 31, 36, 33, 40] #[random.randint(12, 47) for i in range(1, 16)]

def swap(i, j): #interchange element
    t=arr[i]
    arr[i]=arr[j]
    arr[j]=t

def partition(i, j): #return partition value
    l = i+1
    r = j
    c = 'continue'
    while c == 'continue':
        while l <= r and arr[l] <= arr[i]:
            l += 1
        while arr[r] >= arr[i] and r >= l:
            r -= 1
        if r < l:
            c = 'discontinue'
        else:
            swap(l, r)
    swap(i, r)
    return r

def quick_sort(start, stop):
    if start < stop:
        p = partition( start, stop)
        quick_sort(start, p-1) #recursion
        quick_sort(p+1, stop) #recursion
    return arr

print 'sorted list:',quick_sort(0,len(arr)-1)
