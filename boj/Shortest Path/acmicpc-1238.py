from heapq import heappop, heappush
maxCost = float('inf')

N,M,X = map(int,input().split())
Graph=[ [0 for _ in range(N+1)] for _ in range(N+1) ]
ReGraph=[ [0 for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(M):
    u,v,c= map(int,input().split())
    Graph[u][v]=c
    ReGraph[v][u]=c
    
def dij(start, G):
    visited=[-1 for _ in range(N+1)]
    dist=[maxCost for _ in range(N+1)]
    dist[start]=0
    heap=[]
    
    heappush(heap, [0, start])
    
    while heap:
        cost, node = heappop(heap)
        if visited[node]!=1:
            visited[node]=1
            
            for next in range(1,N+1):
                if node!=next and visited[next]==-1 and G[node][next]!=0:
                    if dist[next] >= G[node][next] + cost:
                        dist[next] = G[node][next] + cost
                        heappush(heap, [dist[next], next])
                        
    
    return dist

toParty = dij(X, Graph)
fromParty = dij(X, ReGraph)
sol=0
for i in range (1, N+1):
    tmp = toParty[i]+ fromParty[i]
    sol= max(sol, tmp)
print(sol)