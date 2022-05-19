# 내 선물을 받아줘 (union-find)  sol220513
N,M = map(int,input().split())
G = []
for i in range(N):
    line = input()
    G.append(line)

p= [ [ [-1,-1 ]for _ in range(M) ] for _ in range(N)]

def find(x,y):
    if p[x][y] == [-1,-1] :
        return [x,y]
    
    
    p[x][y] = find(p[x][y][0], p[x][y][1])
    return p[x][y]
    
def union(x,y, nx,ny):
    px,py = find(x,y)
    pnx,pny = find(nx,ny)

    if px == pnx and py ==pny :
        return 
    
    
    p[x][y] = [pnx,pny]


def DFS(x,y):

    visited[x][y]=1
    
    if G[x][y]=='N':
        nx, ny = x-1, y
    elif G[x][y]=='S':
        nx, ny = x+1, y
    elif G[x][y]=='E':
        nx, ny = x,y+1
    elif G[x][y]=='W':
        nx, ny = x,y-1

    if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
        union(nx,ny,x,y)
        DFS(nx,ny)
        
    
visited= [ [0 for _ in range(M)] for _ in range(N) ]
for x in range(N) :
    for y in range(M):
        if visited[x][y]==0 :
            DFS(x,y)

sol = 0
for i in range(N):
    for j in range(M):
        if p[i][j]==[-1,-1]:
            sol+=1

print(sol)