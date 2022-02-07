#Mazzze
from collections import deque
import itertools
graph=[[]for _ in range(5)]
for i in range(5):
    for _ in range(5):
        graph[i].append(list(map(int, input().split())))

    
maze=[[]for _ in range(5)]
dft=[[]for _ in range(5)]

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]

def BFS():
    q = deque([[0,0,0]])
    
    visited= [[ [0 for _ in range(5)] for _ in range(5) ] for _ in range(5)]
    
    while q :
        z,x,y=q.popleft()
        
        
        if z==4 and x==4 and y==4 :
            return visited[4][4][4]
        
        for i in range(6):
            nz,nx,ny = z+dz[i], x+dx[i], y+dy[i]

            if 0<=nz<5 and 0<=nx<5 and 0<=ny<5 and maze[nz][nx][ny]==1 and visited[nz][nx][ny]==0:
                visited[nz][nx][ny] = visited[z][x][y] + 1
                q.append([nz,nx,ny])
                
    return (126)


def turnNo(old):
    return old
    
def turnRight(old):
    new = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = old[j][4-i]
            
    return new

def turnLeft(old):
    new = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = old[4-j][i]
            
    return new


def turnHalf(old):
    new = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            new[i][j] = old[4-i][4-j]
            
            
    return new

floor = list(itertools.permutations([0,1,2,3,4],5))
result = list(itertools.product(([0,1,2,3]), repeat=5))   
sol=126
count=0


for comb in floor:
    for j in range(5):
        dft[j]= graph[ comb[j] ]


    for prmtn in result:
        for i in range(5):
            
            if prmtn[i] == 0:
                maze[i]=turnNo(dft[i])
                
            elif prmtn[i] == 1:
                maze[i]=turnRight(dft[i])
                
            elif prmtn[i]== 2:
                maze[i]=turnHalf(dft[i])
            
            elif prmtn[i] == 3:
                maze[i]=turnLeft(dft[i])
        

        if maze[4][4][4] == 0 or maze[0][0][0] == 0 :
            pass
        else:
            tmp = BFS()
            sol = min(sol, tmp)

  
if sol==126:
    print(-1)
else:
    print(sol)