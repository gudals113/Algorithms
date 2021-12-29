from collections import deque

N, M = map(int, input().split())
miro=[[0 for _ in range(M) ] for _ in range(N)]
for i in range(N):
    line=input()
    for j in range(M):
        miro[i][j]=int(line[j])

visited=[[0 for _ in range(M) ] for _ in range(N)]
visited[0][0]=1
q=deque([])
q.append([0,0])

dx=[-1,1,0,0]
dy=[0,0,-1,1]


prev=[[0 for _ in range(M) ] for _ in range(N)]

while (q):
    x,y=q.popleft()
    if x==N-1 and y==M-1:
        break
    
    for k in range(4):
        nx=x+dx[k]
        ny=y+dy[k]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0 and miro[nx][ny]==1: 
            prev[nx][ny]=(x,y)
            visited[nx][ny]=1
            q.append([nx,ny])

a=N-1
b=M-1    
sol=1
while True:
    sol+=1
    if prev[a][b]==(0,0):
        break
    a,b=prev[a][b]
print(sol)