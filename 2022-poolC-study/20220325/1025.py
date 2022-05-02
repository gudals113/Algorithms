#제곱수 찾기
import math
from pydoc import visiblename
# print(math.sqrt(999999999))
N,M = map(int,input().split())


G=[]
for i in range(N):
    line = input()
    G.append(line)
sol = -1

def check(S):
    global sol
    
    f= int(S)
    b= int(S[::-1])
 
 
    if int(f ** 0.5) **2 == f:
        sol = max(sol, f)
    if int(b ** 0.5) **2 == b:
        sol = max(sol, b)
        
    

def DFS(x,y,dx,dy,num):
    
    # print(num)
    check(num)
    
    nx,ny = x+dx, y+dy
    if 0<=nx<N and 0<=ny<M and visited[nx][ny]==0:
        visited[nx][ny]=1        
        DFS(nx,ny,dx,dy, num+G[nx][ny])
        visited[nx][ny]=0
    
visited=[ [0 for _ in range(M)] for _ in range(N) ]
for x in range(N):
    for y in range(M):
        for i in range(0,N):
            for j in range(-M,M):
                visited[x][y]=1
                DFS(x,y,i,j,G[x][y])
                visited[x][y]=0
print(sol)  