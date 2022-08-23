#성곽
# sol 220824
# BFS, bitmasking

from collections import deque


N, M = map(int, input().split())
G = []
for _ in range(M):
    l = list(map(int, input().split()))
    G.append(l)

dx=[0,-1,0,1]
dy=[-1,0,1,0]
visited = [[ 0 for _ in range(N)]for _ in range(M)]
size = {}

def check(bitNum):

    tmp =[]
    for i in range(4):
        if bitNum & 1<<i ==0 :
            tmp.append(i)
    return tmp

def BFS(a,b,roomNum):
    global size
    q = deque([[a,b]])
    while q:
        x,y = q.popleft()
        bitWall = G[x][y]
        goList = check(bitWall)
        for d in goList:
            nx,ny =  x+dx[d], y+dy[d]
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = roomNum
                size[roomNum]+=1
                q.append([nx,ny])
         
roomNum = 0
maxSize = 0
for x in range(M):
    for y in range(N):
        if not visited[x][y]:
            roomNum+=1
            size[roomNum]=1
            visited[x][y] = roomNum
            BFS(x,y,roomNum)
            
            maxSize = max(maxSize,size[roomNum])
sumSize = 0
for x in range(M):
    
    for y in range(1,N):
        now = visited[x][y]
        next = visited[x][y-1]
        if now!=next:
            sumSize = max(sumSize,size[now]+size[next] )
for y in range(N):
    for x in range(1,M):
        now = visited[x][y]
        next = visited[x-1][y]
        if now!=next:
            sumSize = max(sumSize, size[now]+size[next]) 
    

print(roomNum)
print(maxSize)
print(sumSize)