# boj-1405.py backtracking
# 미친 로봇, sol 220708 poolc study.
from collections import deque


L = list(map(int, input().split()))
N = L[0]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
percent = [ L[1]/100, L[2]/100, L[3]/100, L[4]/100 ]

visited= [ [0 for _ in range(2*N+1)] for _ in range(2*N+1) ]
visited[N][N]=1
sol = 0
def DFS(x,y,tmp,left):
    global visited,sol
    
    if left==0:
        sol+=tmp
        return

    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        np = percent[i]
        
        if visited[nx][ny]==0:
            visited[nx][ny]=1
            DFS(nx,ny,tmp*np,left-1)
            visited[nx][ny]=0
    
            
    
DFS(N,N,1,N)

print(sol)