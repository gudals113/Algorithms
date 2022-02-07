#전쟁 - 전투(BFS)
from collections import deque


N,M = map(int, input().split())
war =[]

for i in range(M):
    war.append(input())



visited=[[0 for _ in range(N)] for _ in range(M)]

dx,dy=[0,0,1,-1], [1,-1,0,0]
def BFS(a,b):
    q=deque([[a,b]])
    word = war[a][b]
    count = 0
    while (q):
        x,y = q.popleft()
        count+=1
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<M and 0<=ny<N and visited[nx][ny]==0 and war[nx][ny] == word: 
                visited[nx][ny]=1
                q.append([nx,ny])
                
    return count   

tmp_w=0
tmp_b=0
for i in range(N*M):
    x = i // N
    y = i % N
    
    if visited[x][y]==0:
        visited[x][y]=1
        tmp = BFS(x,y)
        if war[x][y]=='W':
            tmp_w += tmp**2
        else:
            tmp_b += tmp**2
            
print(tmp_w)
print(tmp_b)