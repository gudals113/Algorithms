#도로포장(다익스트라)
from heapq import heappop, heappush

INF = float('inf')
N,M,K = map(int, input().split())
G=[ [] for _ in range(N+1)]
for _ in range(M):
    u,v,c = map(int,input().split())
    G[u].append([v,c])
    G[v].append([u,c])
    
def dijkstra():
    
    dist=[ [INF for _ in range(K+1)] for _ in range(N+1)]
    visited=[[0 for _ in range(K+1)] for _ in range(N+1)]
    # visited=[0 for _ in range(N+1)]
    heap=[]
    dist[1] = [0 for _ in range(K+1)]
    heappush(heap, [0,0,1])
    
    while heap:
        cum, deleted,node = heappop(heap) #dist[node][deleted], deleted, node
        if visited[node][deleted]==1:
        # if visited[node]==1:
            continue
        
        visited[node][deleted]=1
        # visited[node]=1
        
        for next, cost in G[node]:
            if visited[next][deleted]==1:
            # if visited[next]==1:
                continue
            
            if deleted<K :
                if dist[next][deleted+1] > cum:
                    dist[next][deleted+1]=cum
                    heappush(heap, [cum, deleted+1, next])
                
            if deleted==0:
                if dist[next][deleted] > cum + cost:
                    dist[next][deleted] =cum + cost
                    heappush(heap, [dist[next][deleted], deleted, next])
                
            else:
                if dist[next][deleted] > cum + cost or (dist[next][deleted] > dist[node][deleted-1]+0 ):
                    
                    if cum+ cost > dist[node][deleted-1] :
                        dist[next][deleted] = dist[node][deleted-1]
                        heappush(heap, [dist[next][deleted], deleted, next ])
                    else :
                        dist[next][deleted] = cum + cost
                        heappush(heap, [dist[next][deleted], deleted, next])
                    
    return dist

result = dijkstra()
print(min(result[N]))                      