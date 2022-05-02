L,C = map(int,input().split())
A = list(input().split())

A.sort()

dict={'a':1,'e':1,'i':1,'o':1,'u':1}

def check(w):
    mo = 0
    za = 0
    
    for i in range(L):
        if w[i] in dict :
            mo += 1
        
        else:
            za+=1
    
    if mo>=1 and za >=2 :
        return True
    else:
        return False

sol=[]
word=''
def DFS(idx):
    global word
    
    
    
    # print(word)
    if idx == C :
        if len(word)==L and check(word) :
            sol.append(word)
        return
    
    word += A[idx]
    DFS(idx+1)
    word = word[:-1]
    
    DFS(idx+1)
    

DFS(0)
for i in range(len(sol)):
    
    print(sol[i])
