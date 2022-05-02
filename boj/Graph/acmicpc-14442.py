#벽 부수고 이동하기 2
from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
G=[[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    line = input()
    for j in range(M):
        G[i][j] = int(line[j])


dx,dy=[0,0,1,-1], [1,-1,0,0]
visited=[[[0 for _ in range(K+1)] for _ in range(M)]for _ in range(N)] #해당 칸 벽일 때 


def BFS():
    q=deque([[0,0,0]])
    visited[0][0][0]=1
    while q:
        x,y, br = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:
                
                if G[nx][ny]==0:
                    if visited[nx][ny][br] ==0 :
                        visited[nx][ny][br] = visited[x][y][br]+1
                        q.append([nx,ny,br])
                    
                else:
                    if br<K:
                        if visited[nx][ny][br+1]==0:
                            visited[nx][ny][br+1] = visited[x][y][br]+1
                            q.append([nx,ny,br+1])
                    
                
                # if br==K:
                #     if G[nx][ny]==0:
                #         if visited[nx][ny][K]==0:
                #             visited[nx][ny][K]= visited[x][y][K]+1
                #             q.append([nx,ny,br])
                        
                # else:
                #     if G[nx][ny]==0:
                #         if visited[nx][ny][br]==0:
                #             visited[nx][ny][br] = visited[x][y][br]+1
                #             q.append([nx,ny,br])

                #     elif G[nx][ny]==1:
                #         if visited[nx][ny][br+1]==0:
                #             visited[nx][ny][br+1]=visited[x][y][br]+1
                #             q.append([nx,ny,br+1])
BFS()
sol=1000001
for i in range(K+1):
    tmp = visited[N-1][M-1][i]
    if tmp > 0:
        sol = min(sol, tmp)
        
if sol==1000001:
    print(-1)
else:
    print(sol)