# Created on: 2019-10-19
# @author: Deepak Singh

# user input.......
arr = [6, 91, 27, 61, 67, 12, 91, 58, 44, 70, 98, 84, 34, 21, 63, 41, 15, 65, 92, 28, 28, 54, 5, 51, 48, 33, 46, 98, 68, 71]

# Change '<' to '>' for decreasing sequence
comparator = lambda x,y: x < y

# Iterative function for LIS
def LIS_i(arr):
    n, max_seq_len = len(arr), 1
    table = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i <= j:
                table[j].append(1)
            else:
                if comparator(arr[j], arr[i]):
                    elt = 1+max((table[k][j] for k in range(j+1)))
                    max_seq_len = max(max_seq_len, elt)
                    table[j].append(elt)
                else:
                    table[j].append(0)
    return max_seq_len

# Recursive function for LIS
n, max_seq_len = len(arr), 1
table = [[] for _ in range(n)]
def LIS_r(i=0, j=0):
    global max_seq_len
    if i <= j:
        table[j].append(1)
    else:
        if comparator(arr[j], arr[i]):
            elt = 1+max((table[k][j] for k in range(j+1)))
            max_seq_len = max(max_seq_len, elt)
            table[j].append(elt)
        else:
            table[j].append(0)
    if i < n-1:
        LIS(i+1, j)
    elif j < n-1:
        LIS(0, j+1)
    return max_seq_len
