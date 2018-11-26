# reverse an integer

n = 7654321 #input('Type a number ')
s = 0
while n > 0:
    r = n%10 #Remainder
    s = s*10+r
    n = (n-r)/10 #Update number
print s
    
