#피리 부는 사나이 union/find
def find(u):
    if p[u]<0:
        return u
    p[u]= find(p[u])
    return p[u]
def union(u,v) :
    u,v = find(u), find(v)
    if u==v:
        return
    
    p[u]=v
    
N, M = map(int, input().split())
G = []
for i in range(N):
    G.append(input())

visited=[ [ 0 for _ in range(M)]for _ in range(N)]
p=[ -1 for _ in range(N*M)]


def DFS(idx):
    x,y =idx//M, idx%M
    now = G[x][y]
    
    if now=='U' and x-1 >=0:
        union(idx, idx-M )
        if visited[x-1][y]==0:
            visited[x-1][y]=1
            DFS(idx-M)
            
        
    elif now=='D' and x+1 <N :
        union(idx, idx+M)
        if visited[x+1][y]==0:
            visited[x+1][y]=1
            DFS(idx+M)

    
    elif now=='L' and y-1 >=0 :
        union(idx, idx-1)
        if visited[x][y-1]==0:
            visited[x][y-1]=1
            DFS(idx-1)
              
        
        
    elif now=='R' and y+1 <M :
        union(idx, idx+1)
        if visited[x][y+1]==0:
            visited[x][y+1]=1
            DFS(idx+1)
    
    return

for i in range(N*M):
    x,y =i//M, i%M
    if visited[x][y]==0:
        DFS(i)
        
sol=0
for root in p:
    if root==-1:
        sol+=1
print(sol)

    
#방문한 경우라도 중간에 만나면 하나의 집합으로 만들어주는것(union)이 핵심인 문제다.