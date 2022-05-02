N,M = map(int,input().split())
R,C,D = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int,input().split())))

visited=[ [0 for _ in range(M)] for _ in range(N) ]

def checkLeft(x,y,d,turn):
    if turn ==4:
        return x,y,d,turn
    
    if d==0:
        if 0<=y-1 and G[x][y-1]==0 and visited[x][y-1]==0:
            return x,y-1,3 ,turn
        else:
            t1,t2,t3,t4 = checkLeft(x,y,3,turn+1)
            return t1,t2,t3,t4
    
    elif d==1:
        if 0<=x-1 and G[x-1][y]==0 and visited[x-1][y]==0:
            return x-1,y,0,turn
        else:
            t1,t2,t3,t4 = checkLeft(x,y,0,turn+1)
            return t1,t2,t3,t4
    
    elif d==2:
        if y+1<M and G[x][y+1]==0 and visited[x][y+1]==0:
            return x,y+1,1,turn

        else:
            t1,t2,t3,t4 = checkLeft(x,y,1,turn+1)
            return t1,t2,t3,t4
    
    elif d==3:
        if x+1<N and G[x+1][y]==0 and visited[x+1][y]==0:
            return x+1, y, 2, turn
        else:
            t1,t2,t3,t4 = checkLeft(x,y,2,turn+1)
            return t1,t2,t3,t4

def checkBack(x,y,d):
    if d==0:
        if x+1<N and G[x+1][y]==0 :
            return x+1,y
        
        else:
            return x,y
    
    elif d==1:
        if 0<=y-1 and G[x][y-1]==0:
            return x,y-1
        else:
            return x,y
    elif d==2:
        if 0<=x-1 and G[x-1][y]==0:
            return x-1,y
        else:
            return x,y
    elif d==3:
        if y+1<M and G[x][y+1]==0:
            return x,y+1
        else:
            return x,y

sol=0

def DFS(x,y,d):
    global sol
    
    if visited[x][y]==0:
        visited[x][y]=1
        sol+=1
    
    
    nx,ny,nd,turned = checkLeft(x,y,d,0)
    
    if turned ==4:
        nnx,nny = checkBack(nx,ny,nd)
        
        if nnx==nx and nny == ny:
            return False
        
        else:
            DFS(nnx,nny,nd)
    
    else:
        DFS(nx,ny,nd)
    
DFS(R,C,D)
print(sol)