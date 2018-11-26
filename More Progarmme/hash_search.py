# Implementation of hash search

# random array
arr = [39, 37, 35, 36, 35, 36, 47, 44, 32, 39, 40, 31, 36, 33, 40]

# type a number which you wanna search in above array
x = 47

def prime(n): #provide n prime number list
    arr = [2,3]
    b = [3]
    k = 5
    while len(arr) < n:
        if arr[len(b)]**2 <= k:
            b += [arr[len(b)]]
        for j in b:
            if k%j == 0:
                k += 2
                break
        if (j == b[len(b)-1]) and k%j != 0:
            arr += [k]
            k += 2
    return arr

def filter_prime(p): #filter primes >= list size
    if p >= len(arr):
        return p

def compression_map(arr=[]): #provide compressed list
    for k in filter(filter_prime,prime(2*len(arr))):
        t = 'prime'
        b = [[]]*k #list of empty lists 
        for i in arr:
            j = i%k
            if b[j] != []:
                while b[j] != []:
                    if j == len(arr)-1:
                        t = 'new_prime'
                        break
                    j += 1
            if t == 'new_prime':
                break
            b[j] = i
        if i == arr[len(arr)-1]:
            break
    return b

def hash_function(x): #search for arr number
    n_a = compression_map(arr)
    h = len(compression_map(arr))
    j = x%h
    for i in range(j,len(n_a)):
        if n_a[i] == x:
            return '%d lies in the list '%x
        elif (n_a[i] == []) or (i == len(n_a)):
            return '%d does not lies in the list '%x
        else:
            continue

print hash_function(x)
