# Perform binary search in provided python list

# Provide your list (It should be sorted)
arr = [64, 66, 69, 70, 82, 82, 88, 90, 91, 93]

# Provide your number which you want to search
num = 70 

# Calculate middle index
def m_pos(m):
    if m%2 == 0:
        m = m/2
    else:
        m = (m+1)/2
    return m

def binary_search(num, a = []):
    i = -1
    j = len(a)
    q = '%d does not lie in list'%num
    while j-i != 1:
        if num < a[m_pos(j+i)]:
            j = m_pos(j+i)
        elif num > a[m_pos(j+i)]: 
            i = m_pos(j+i)
        else:
            q = '%d lies in list'%num
            break
    return q
print binary_search(num, arr)
