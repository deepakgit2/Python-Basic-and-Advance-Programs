# This programme convert a decimal to any provided base

num = 10 #input('type decimal no. ')
base = 2 #input('type base ')
a=[]
def f(t=[]):
    su=0
    for i in range(len(t)-1,-1,-1):
        su=su*10+t[i]
    return su
while num > 0:
    r = num%base
    num = num/base
    a = a + [r] #Collect all remainder
print f(a)
