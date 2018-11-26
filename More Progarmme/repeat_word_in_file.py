# Return the word count in given file

f = open('repeating_word_in_file_help.txt','r+')
z = 'this' #input('Type a word in string ') #search keyword
def word_list(s=''): #Count each word in file
    w = ''
    w_l = {}
    for i in range(len(s)):
        if s[i] in " ,\'\":()?.\n" or (i==len(s)):
            if w != '':
                if w in w_l:
                    w_l['%s'%w] = w_l['%s'%w]+1
                else:
                    w_l['%s'%w] = 1
            w = ''
        else:
            w += s[i]
    return w_l
d = word_list(f.read())
if z in d:
    print 'Counting of \'%s\' in file is'%z,d[z]
else:
    print '\'%s\' does not lie in file'%z
f.close()
