# It perform a sublinear pattern search algorithm on given text file

f = open('sublinear_pattern_search_help.txt','r+')
pattern = 'lion'

def match(j,pattern='',s=''):
    l = len(pattern)-2
    for i in range(l,-1,-1):
        if pattern[i] == s[j-1]:
            j -= 1
        else:
            return 
    return 'match'

def skip(j,pattern='',s=''):
    l=len(pattern)-2
    for i in range(l,-1,-1):
        if pattern[i] != s[j]:
            continue
        else:
            return l-i+1

def sublinear(pattern,s):
    l = len(pattern)
    j = len(pattern)-1
    while j < len(s):
        if s[j] not in pattern:
            j += l
        elif s[j] == pattern[l-1]:
            if match(j,pattern,s) == 'match':
                return 'match found'
            else:
                j += l
        else:
            j += skip(j,pattern,s)
    return 'match not found'

print sublinear(pattern,f.read())
f.close()
