#벽 부수고 이동하기 4 (union-find로 0 개수 저장)
#flood fill 알고리즘?
from collections import deque
import sys
input = sys.stdin.readline
def find(u):
    if p[u]<0:
        return u
    
    p[u]=find(p[u])
    return p[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v:
        return 
    
    p[u]+=p[v]
    p[v]=u
    
    
N, M = map(int,input().split())
G=[ [0 for _ in range(M)] for _ in range(N)]
SOL= [[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(M):
        G[i][j] = int(l[j])
    
#visited애 0 개수 역추적해서 저장 / union find해서 저장
visited=[ [0 for _ in range(M)]for _ in range(N) ] 
p=[-1 for _ in range(M*N)]
def countBFS(idx):
    x,y = idx//M, idx%M
    q=deque([ [x,y] ])
    while q:
        x,y = q.popleft()
        
        for nx,ny in [ [x+1,y], [x-1,y], [x,y+1], [x,y-1] ] :
            if nx>=0 and nx<N and ny>=0 and ny<M :
                if G[nx][ny]==0:
                    if visited[nx][ny]==0:
                        visited[nx][ny]=1
                        q.append([nx,ny])
                        union( idx, nx*M+ny )

def solBFS(idx):
    sol=-1
    root=[]
    x,y = idx//M, idx%M
    for nx,ny in [ [x+1,y], [x-1,y], [x,y+1], [x,y-1] ] :
        if nx>=0 and nx<N and ny>=0 and ny<M :
            if G[nx][ny]==0:
                node=find(nx*M+ny)
                if node not in root:
                    root.append(node)
    
    for node in root:
        sol+= p[node]
    return abs(sol)
                
for i in range(N*M):
    x,y = i//M, i%M
    if G[x][y]==0 and visited[x][y] ==0:
        visited[x][y]=1
        countBFS(i) 

for i in range(N*M):
    x,y = i//M, i%M
    if G[x][y]==1 and visited[x][y]==0:
        visited[x][y]=1
        SOL[x][y] = solBFS(i) %10
            
for i in range(N):
    print(''.join(map(str, SOL[i])))