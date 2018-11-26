from combination_generation import recursion, init_permut, combination

n=input('Type integer ')
a=list(range(1,n+1))
r=input('Type number of place(greater than 1) ')
k=0
def exchange(a,i,j):
    t=a[i]
    a[i]=a[j]
    a[j]=t
    
def f(n):
    if n==0:
        return 1
    else:
        return n*f(n-1)
def permutation(a):
    l=len(a)
    global k
    while k!=f(len(a)):
        for i in range(l-1):
            k+=1
            print a
            exchange(a,i,i+1)
        permutation(a)
n_list=recursion(init_permut(a),r)
for x in n_list:
    permutation(x)
    k=0
