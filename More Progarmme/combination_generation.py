# This programme generates all combination

a = list(range(1, 4))
r = 2

def combination(b):
    n_a = []
    l = len(a)
    for z in b:
        for i in a[z[len(z)-1]:]: #slicing of list
            n_a.append(z+[i])
    return n_a

def init_permut(a):
    b = []
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            b += [[a[i],a[j]]]
    return b

def recursion(q,r): #recursion goes here
    if len(q[0])<r:
        p = combination(q)
        return recursion(p,r)
    return q

print recursion(init_permut(a),r)
