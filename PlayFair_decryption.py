# This program encrypt the sentence using play fair cypher technique

# Type your encryoted massage here (e.g e_msg is encrypted by "TextForEncyption" )
e_msg='WCZVOVQYTDCLZPQO'
# Your Public key for decryption
key='PublicKey'

alph='ABCDEFGHIKLMNOPQRSTUVWXYZ'
def dup(s=''):
    if 'j' in s:
        s=s.replace('j','i')
    n_s=''
    for i in s:
        if i not in n_s:
            n_s=n_s+i
    return n_s.upper()
m_key=dup(key)
for k in alph:
    if k not in m_key:
        m_key=m_key+k
        
def pair(s=''):
    l_s=list(s.upper())
    j=0
    while j<len(l_s)-1:
        if l_s[j]==l_s[j+1]:
            l_s.insert(j+1,'X')
        j=j+2
    if len(l_s)%2!=0:
        l_s.append('X')
    return l_s

def vec2mat(a):
    t_a=[]
    for i in range(0,25,5):
        t=list(a[i:i+5])
        t_a=t_a+[t]
    return t_a

def ind(a,x):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==x:
                return i,j
    return 'does not exist'

k_mat=vec2mat(m_key)
decrypt=''
for i in range(0,len(e_msg),2):
    if ind(k_mat,e_msg[i])[0]==ind(k_mat,e_msg[i+1])[0]:
        x=k_mat[ind(k_mat,e_msg[i])[0]][(ind(k_mat,e_msg[i])[1]-1)%5]
        y=k_mat[ind(k_mat,e_msg[i+1])[0]][(ind(k_mat,e_msg[i+1])[1]-1)%5]
    elif ind(k_mat,e_msg[i])[1]==ind(k_mat,e_msg[i+1])[1]:
        x=k_mat[(ind(k_mat,e_msg[i])[0]-1)%5][ind(k_mat,e_msg[i])[1]]
        y=k_mat[(ind(k_mat,e_msg[i+1])[0]-1)%5][ind(k_mat,e_msg[i+1])[1]]
    else:
        x=k_mat[ind(k_mat,e_msg[i])[0]][ind(k_mat,e_msg[i+1])[1]]
        y=k_mat[ind(k_mat,e_msg[i+1])[0]][ind(k_mat,e_msg[i])[1]]
    decrypt=decrypt+x+y
print(decrypt)
