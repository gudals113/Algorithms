#벽 부수고 이동하기 
from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
G=[[0 for _ in range(M)]for _ in range(N)]
for i in range(N):

    line = input()
    for j in range(M):
        G[i][j] = int(line[j])

dx,dy=[0,0,1,-1], [1,-1,0,0]
visited=[[[0 for _ in range(2)] for _ in range(M)]for _ in range(N)] #해당 칸 벽일 때 

def BFS():
    q=deque([[0,0,0]])
    visited[0][0][0]=1
    while q:
        x,y, br = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if nx>=0 and nx<N and ny>=0 and ny<M:

                if br==1:
                    if G[nx][ny]==0:
                        if visited[nx][ny][1]==0:
                            visited[nx][ny][1]= visited[x][y][1]+1
                            q.append([nx,ny,br])
                        
                else:
                    if G[nx][ny]==0:
                        if visited[nx][ny][0]==0:
                            visited[nx][ny][0] = visited[x][y][0]+1
                            q.append([nx,ny,br])

                    elif G[nx][ny]==1:
                        if visited[nx][ny][1]==0:
                            visited[nx][ny][1]=visited[x][y][0]+1
                            q.append([nx,ny,br+1])
BFS()

br_no=visited[N-1][M-1][0]
br_yes=visited[N-1][M-1][1]
if br_no == 0 and br_yes ==0:
    print(-1)
elif br_no==0:
    print(br_yes)  
elif br_yes==0:
    print(br_no)
else:
    print(min (br_no, br_yes))
    
    

# bfs 돌리다가.
# 특정 칸에 / 벽을 부수고 왔는데 벽을 안부수고 온 애랑 똑같이 도착 
# - > 벽을 부수고 온애는 visited[x][y][1]에따로 저장 // 안부수고 온 애는 visited[x][y][0]에 저장
# 근데 그래도 도착했는데 이미 있는 경우가 있나?
# 8 8
# 01000100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 01010100
# 00010100