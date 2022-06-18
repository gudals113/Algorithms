from collections import defaultdict


N = int(input())
G = [ list(map(int, input().split())) for _ in range(N)]

answer=defaultdict(int)

def check(x,y, lenght):
        
    tmp = G[x][y]
    
    if lenght==1:
        answer[tmp]+=1
        return
    
    div = 0
    for i in range(x, lenght+x):
        if div==1:
            break
        for j in range(y,lenght+y):
            if G[i][j] != tmp :
                div = 1
                break
        
    if div ==1:
        for i in [0,lenght//3, 2*lenght//3 ]:
            for j in [0,lenght//3, 2*lenght//3 ]:
                check(x+i,y+j,lenght//3)
        
    
    else:
        answer[tmp]+=1
        return

check(0,0,N)
    
            
print(answer[-1])
print(answer[0])
print(answer[1])
    
    