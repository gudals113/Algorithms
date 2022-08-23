# 감소하는 수
# 220803 hint
# 백트래킹
N = int(input())
L =[]

def DFS(tmp, start):

    if start==-1:
        return
    

    for plus in range(start,-1,-1):
        newStr = tmp+str(plus)
        DFS(newStr, plus-1)
        
        L.append(int(newStr))

DFS('', 9)
L.sort()
if N>len(L)-1:
    print(-1)
else:
    
    print(L[N])