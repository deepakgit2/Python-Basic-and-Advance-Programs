# It perform a linear pattern search algorithm on given text file

f = open('linear_pattern_search_help.txt','r+') #Open file
pattern = '[ [ [ ] ] ] ] ]'

def p_s(pattern,s):
    i = 0
    j = 0
    while j < len(s):
        if pattern[i] == s[j]:
            i += 1
            if i == len(pattern):
                return 'Pattern Found'
        else:
            i = 0
        j = j+1
    return ' Pattern Not Found'

print p_s(pattern,f.read())
f.close() #Close file
