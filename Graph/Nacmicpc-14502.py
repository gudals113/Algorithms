#미제출, 벽 세우는 부분 힌트 얻어서 풀었음
from collections import deque
import copy


N,M = map(int, input().split())
lab=[]
virus=[]
visited=[[-1 for _ in range(M)] for _ in range(N)]
wall = 0
sol=0

for i in range(N):
    line = list( map(int, input().split()) )
    for j in range(M):
        if line[j]==2:
            virus.append([i,j])
        elif line[j]==1:
            wall+=1
    lab.append( line )

dx, dy = [0,0,1,-1], [1,-1,0,0]


def bfs():
    global sol
    notsafe=len(virus)
    visited = copy.deepcopy(lab)
    
    for v in virus:
        q=deque([])
        q.append(v)
        while (q):
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
                    notsafe+=1
                    visited[nx][ny]=2
                    q.append([nx,ny])
    sol=max(sol, N*M - wall -3 - notsafe)
    return
            
            
        

def build(wall):
    if wall == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if lab[i][j]==0:
                lab[i][j]=1
                build(wall+1) 
                lab[i][j]=0
    
build(0)
print(sol)
 
