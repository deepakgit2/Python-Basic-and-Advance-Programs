# In recursion we do wasteful recomputation
# Memoization is a better solution. In this process we store the computed value
# so that we can reuse rather than recmpute

# Memory table for factorial and fibbonacci
fact_memory = [1]
fibo_memory = [0, 1]

def fact(n):
    try:
        return fact_memory[n]
    except IndexError:
        pass
    
    fact_memory.append(n*fact(n-1))
    return fact_memory[-1]


def fibo(n):
    try:
        temp = fibo_memory[n-1] + fibo_memory[n-2]
        if n == len(fibo_memory):
            fibo_memory.append(temp)
        return temp
    except IndexError:
        pass
    
    value = fibo(n-1) + fibo(n-2)
    fibo_memory.append(value)
    return value

print fact(5)   
print fibo(5)