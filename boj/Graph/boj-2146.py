# 220804 10:53
# 다리 만들기
# BFS
import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
N = int(input())
G=[]
for _ in range(N): G.append( list(map(int,input().split())) )

def BFS(a,b,landIdx):
    q = deque([[a,b]])
    while q:
        x,y =q.popleft()
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<N and G[nx][ny]==1 and not numG[nx][ny]:
                numG[nx][ny]=landIdx
                q.append([nx,ny])

numG=[[ 0 for _ in range(N)]for _ in range(N)]
start=[]
landIdx = 0
for x in range(N):
    for y in range(N):
        if G[x][y]==1 and not numG[x][y]:
            landIdx+=1
            numG[x][y]=landIdx
            start.append([x,y,landIdx])
            BFS(x,y,landIdx)

answer = INF

def findBFS(a,b,landIdx):
    global answer
    visited[a][b]=0
    q = deque([[a,b]])
    
    while q:
        x,y = q.popleft()
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<N :
                if numG[nx][ny]==landIdx and visited[nx][ny]==INF :
                    visited[nx][ny] = 0 
                    q.append([nx,ny])
                    
                elif numG[nx][ny]==0 and visited[nx][ny] > visited[x][y]+1 :
                    visited[nx][ny] = visited[x][y]+1
                    q.append([nx,ny])
                
                elif numG[nx][ny]!=0 and numG[nx][ny] != landIdx and visited[nx][ny] > visited[x][y]+1:
                    visited[nx][ny] = visited[x][y]+1
                    answer= min(answer, visited[nx][ny])

visited=[[INF for _ in range(N)]for _ in range(N)]
for x,y,num in start:
    findBFS(x,y,num)
print(answer-1)
        