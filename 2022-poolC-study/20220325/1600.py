#말이되고 싶은 원숭이
from collections import deque


K= int(input())
W, H = map(int,(input().split()))
G = []
for _ in range(H):
    G.append( list(map(int, input().split())) )
    
    
dx=[-2,2,-1,1,-2,2,-1,1]
dy=[1,1,2,2,-1,-1,-2,-2]   

visited=[[[0 for _ in range(K+1)] for _ in range(W)]for _ in range(H)]
def BFS():
    q= deque([[0,0,0]])
    

    while q:

        x,y,use = q.popleft()
        if x == H-1 and y == W-1:
            return visited[x][y][use]
        
        if use < K :
            for i in range(8):
                nx,ny = x+dx[i], y+dy[i]
                
                if 0<=nx<H and 0<=ny<W and G[nx][ny]==0:
                    if visited[nx][ny][use+1] == 0 :
                        visited[nx][ny][use+1] = visited[x][y][use]+1
                        q.append([nx,ny,use+1])
                 
        for nx,ny in ([x+1,y], [x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<H and 0<=ny<W and G[nx][ny]==0:
                if visited[nx][ny][use] == 0 :
                    visited[nx][ny][use] = visited[x][y][use]+1
                    q.append([nx,ny,use])
    return -1
                    
result = BFS()
print(result)