G=[list(map(int, input().split())) for _ in range(10)]
# visited = [ [0 for _ in range(10)] for _ in range(10) ]
have = [5 for _ in range(6)]

def check(x,y,size):
    for i in range(size):
        for j in range(size):
            nx,ny = x+i, y+j
            if nx<0 or nx>=10 or ny<0 or ny>=10 or G[nx][ny]==0 :
                return False
            
    return True

def isLeft():
    for i in range(10):
        for j in range(10):
            if G[i][j]==1:
                return False
    return True

sol= 26
tmp=0
def DFS(x,y):
    global have,sol,tmp
      
    if x==9 and y>=10:
        if isLeft():
            sol = min(sol, tmp)
        
        return True
    
    if x<9 and y>=10:
        x+=1
        y=0
    
    if G[x][y]==1:
        for k in range(1,6):
            if have[k]>0 and check(x,y,k):
                
                for i in range(k):
                    for j in range(k):            
                        G[x+i][y+j]=0
                tmp+=1
                have[k]-=1
                
                DFS(x,y+k)
                
                for i in range(k):
                    for j in range(k):            
                        G[x+i][y+j]=1       
                tmp-=1        
                have[k]+=1   
        
        if k == 5 and have[k]<=0:
            return False
        
    else:
        DFS(x,y+1)        
    
    return True         


if isLeft():
    print(0)
else:                          
    DFS(0,0)
    if sol == 26:
        print(-1)
    else:
        print(sol)
