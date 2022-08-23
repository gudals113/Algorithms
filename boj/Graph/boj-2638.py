#치즈
#220726 sol
#DFS, BFS
import sys
from collections import deque
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
G = []
chz = deque()
for x in range(N):
    l = list(map(int, input().split()))
    G.append(l)
    
    for y in range(M):
        if l[y]==1:
            chz.append([x,y])
            
def findOutsideDFS(x,y):
    visited[x][y]=1
    for nx, ny  in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<N and 0<=ny<M and G[nx][ny] ==0:
            if not visited[nx][ny]:
                findOutsideDFS(nx,ny)
                
def findMeltingDFS(x,y):
    air = 0
    for nx, ny  in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<N and 0<=ny<M:
            #주위의 4방향에서 방문 표시가 1이고 좌표의 값이 0 이면 외부 공기
            if visited[nx][ny] == 1 :
                air +=1
    return air
     
time = 0
#visited 1:외부 공기
visited= [[0 for _ in range(M)]for _ in range(N)]
findOutsideDFS(0,0)
while chz:
    melting=[]

    T = len(chz)

    for _ in range(T):
        x,y = chz.popleft()
        rst = findMeltingDFS(x,y)
        if rst>=2:
            melting.append([x,y])
            
        else:
            chz.append([x,y])
    
    for x,y in melting :
        G[x][y]=0
    
    for x,y in melting :
        findOutsideDFS(x,y)
        
    time+=1
    
print(time)