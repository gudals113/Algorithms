#다리 만들기 (MST)
from collections import deque

N, M = map(int, input().split())
G=[]
for _ in range(N):
    G.append(list(map(int,input().split())))


def numbering():
    
    visited = [ [0 for _ in range(M)] for _ in range(N) ]
    
    idx = 1
    for x in range(N):
        for y in range(M):
            
            if G[x][y] == 1 and not visited[x][y]:    
                q=deque([[x,y]])
                visited[x][y] = idx
                while q:
                    x,y = q.popleft()
                    for nx,ny in ([x+1,y],[x-1,y], [x,y+1], [x,y-1]) :
                        if 0<=nx<N and 0<=ny<M and G[nx][ny]==1 and visited[nx][ny]==0:
                            visited[nx][ny] = idx
                            q.append([nx,ny])
                            
                    
                idx+=1
    print(visited)
                
numbering()
                    
                
                