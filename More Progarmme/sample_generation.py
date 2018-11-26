n=input('Type number of integer ')
r=input('Type number of  place ')
c=[[]]*r
w=-1
def sample(k):
    global w
    c[k]=0
    while c[k]<n:
        c[k]+=1
        w+=1
        if w%(n+1)!=0:
            print c
        if k<r-1:
            sample(k+1) #recursion
sample(0)
