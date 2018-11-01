# This function multiply two polynomials using cauchy product formula
# Input : a polynomial can be represent by a list where elements 
#         of list are the coefficients of polynomial
# Output : This program return multiplication of two polynomails in list form 

# a = 1 + 2x can be wriiten as following
a = [1, 2, 3]
# b = 1 + x can be wriiten as following
b = [1, 1]

def p_multi(a,b):
    m = len(a)
    n = len(b)
    k = m+n-1
    b +=  [0]*k
    a +=  [0]*k
    m_l = []
    for i in range(k):
        s = 0
        for j in range(i+1):
            s +=  a[j]*b[i-j]
        m_l +=  [s]
    return m_l
    
print(p_multi(a,b))
