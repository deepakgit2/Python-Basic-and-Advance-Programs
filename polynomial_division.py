# div function divide polynomial b by polynomial a
# Input : a polynomial can be represent by a list where elements 
#         of list are the coefficients of polynomial
#Output : This program return remainder and quotient in list form 

# a = 1 + 2x + 3x^2 can be wriiten as following
a = [1, 2, 3]
# b = 1 + x + x^2 + x^3 can be wriiten as following
b = [1, 1, 1, 1]

def sub(a,b):
    n_a = a[:]
    n_b = b[:]
    n_a += [0]*(len(b)-len(a))
    n_b += [0]*(-len(b)+len(a))
    return [n_a[i]-n_b[i] for i in range(len(n_a))]

def mult(k,a,s):  #multiply by k and shift s place
    return [0]*s+[k*i for i in a]

def div(a, b):
    m = len(a)
    quot = []
    while len(b) >= m:
        k = (b[-1])/(a[m-1])
        t = sub(b , mult(k,a,len(b)-m) )
        quot += [k]
        b = t[:-1]
    quot.reverse()
    return 'remainder: {}\nquotient: {}'.format(b,quot)

print(div(a,b))
