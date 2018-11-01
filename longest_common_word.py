# this function is takes two string and return longest common subword
list_1 = ['secret', 'bisect', 'bisect', 'director' ]
list_2 = ['secretary', 'trisect', 'secret', 'secretary']

def LCW(u, v):
    m = len(u)
    n = len(v)
    zeros = [[0]*n]*m

    mx = (0,0)
    for i in range(m):
        for j in range(n):
            if u[i] == v[j]:
                try:
                    value = zeros[i-1][j-1]
                except:
                    value = 0
                zeros[i][j] = value + 1
                if mx[0] < value+1:
                    mx = (value+1, j)
    return v[mx[1]-mx[0]+1:mx[1]+1]

print ('Longest common words are: \n')
for i in range(len(list_1)):
    print LCW(list_1[i], list_2[i])
