# For given n it will generate first n prime number

n = 7 #input('How much prime number u wanna see ')

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
print arr
