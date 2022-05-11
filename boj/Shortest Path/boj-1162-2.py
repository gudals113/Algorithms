
from heapq import heappop, heappush


N,M,K = map(int,input().split())
G=[ [] for _ in range(N+1)]
for _ in range(M):
    u,v,c = map(int, input().split())
    G[u].append([v,c])
    G[v].append([u,c])

INF = float('inf')
heap = []
dist = [ [INF for _ in range(K+1)] for _ in range(N+1)] 
dist[1][0]=0
heappush(heap, [0,1,0]) #cost, node, k
while heap:
    cost, node, k = heappop(heap)
    if dist[node][k] < cost  :
        continue
    
    #2가지 갱신, 길 없애고, 길 안없애고
    for next, weight in G[node]:
        if dist[next][k] > cost+ weight:
            dist[next][k] = cost + weight
            heappush(heap,[ dist[next][k],next, k ])
            
    if k < K :
        for next, weight in G[node] :
            if dist[next][k+1] > cost :
                dist[next][k+1] = cost
                heappush(heap, [ dist[next][k+1], next, k+1 ])            


answer = INF

for i in range(K+1) :
    if dist[N][i] != INF:
        answer = min(answer, dist[N][i])      
print(answer)