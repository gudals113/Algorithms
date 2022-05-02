#도시 왕복하기 2
#정점 분할하기
from collections import deque


N,P = map(int,input().split())
capacity = [ [0 for _ in range(N+1)] for _ in range(N+1) ]
flow = [ [0 for _ in range(N+1)] for _ in range(N+1) ] 
G=[[]for _ in range(N+1)]
for _ in range(P):
    u, v = map(int,input().split())
    
    G[u].append(v)
    G[v].append(u)
    capacity[u][v]=1
    capacity[v][u]=1
    
sol=0

start=1
end=2
while True:
    q=deque([[start]])
    visited=[ 0 for _ in range(N+1)]
    prev=[-1 for _ in range(N+1)]
    while q:
        if prev[1]!=-1:
            break
        
        node= q.popleft()
        
        visited[node]=1
        
        for next in G[node]:

            if visited[next]==0 and capacity[node][next]>flow[node][next] :
                prev[next]=node
                q.append([next])
                
    if prev[end]==-1:
        break
    
    vertex = 1
    count=0
    while True:
        if vertex==1 :
            count+=1
            if count==2:
                break
            
        flow[prev[vertex]][vertex] +=1
        flow[vertex][prev[vertex]] -=1 #이거 없애기
        vertex = prev[vertex]
    
    sol+=1
    
    
print(sol)