# 탈출
# BFS
# sol 220823-24
# 5427번 불 이랑 같은 문제

from collections import deque

R, C = map(int, input().split())
G = [ [0 for _ in range(C)]for _ in range(R)]
q=deque()
gosm=[0,0]
for x in range(R):
    l = input()
    for y in range(C):
        
        #물이면,
        if l[y] == '*' :
            G[x][y] = 1
            q.append([x,y])
        
        #돌이면,
        elif l[y] == 'X':
            G[x][y] = -1
        
        #비버의 굴
        elif l[y] == 'D':
            G[x][y] = -2
                  
        #고슴이 시작      
        elif l[y] == 'S':
            gosm = [x,y]

while q:
    x,y = q.popleft()
    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        #if not visited[nx][ny]
        if 0<=nx<R and 0<=ny<C and G[nx][ny]==0:
            G[nx][ny] = G[x][y] + 1
            q.append([nx,ny])
            
q.append([1, gosm[0],gosm[1]])
answer = 'KAKTUS'
visited = [[0 for _ in range(C)]for _ in range(R)]
visited[gosm[0]][gosm[1]] = 1
while q:
    time , x,y = q.popleft()
    if G[x][y] == -2:
        answer = time-1
        break
    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            if G[nx][ny]==-2 or (G[nx][ny]>time+1) or G[nx][ny]==0:
                visited[nx][ny]=1
                q.append([time+1, nx,ny])

print(answer)
from collections import deque

R, C = map(int, input().split())
G = [ [0 for _ in range(C)]for _ in range(R)]
q=deque()
gosm=[0,0]
for x in range(R):
    l = input()
    for y in range(C):
        
        #물이면,
        if l[y] == '*' :
            G[x][y] = 1
            q.append([x,y])
        
        #돌이면,
        elif l[y] == 'X':
            G[x][y] = -1
        
        #비버의 굴
        elif l[y] == 'D':
            G[x][y] = -2
                  
        #고슴이 시작      
        elif l[y] == 'S':
            gosm = [x,y]

while q:
    x,y = q.popleft()
    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        #if not visited[nx][ny]
        if 0<=nx<R and 0<=ny<C and G[nx][ny]==0:
            G[nx][ny] = G[x][y] + 1
            q.append([nx,ny])
            
q.append([1, gosm[0],gosm[1]])
answer = 'KAKTUS'
visited = [[0 for _ in range(C)]for _ in range(R)]
visited[gosm[0]][gosm[1]] = 1
while q:
    time , x,y = q.popleft()
    if G[x][y] == -2:
        answer = time-1
        break
    for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
        if 0<=nx<R and 0<=ny<C and not visited[nx][ny]:
            if G[nx][ny]==-2 or (G[nx][ny]>time+1) or G[nx][ny]==0:
                visited[nx][ny]=1
                q.append([time+1, nx,ny])

print(answer)