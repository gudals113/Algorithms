#최단경로 다익스트라. 220524
#아마 방문처리를 통해 문제를 푸는 사람들이 많아서 정답 비율이 낮은 것 같다
#21번째 줄처럼 dist의 값으로 비교를하고 문제를 풀어야한다.
from heapq import heappop, heappush

INF = float('inf')
V, E = map(int,input().split())
K = int(input())
G=[[]for _ in range(V+1)]
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u].append([v,w])
    
dist =[INF for _ in range(V+1)]    
heap =[]
dist[K] = 0
heappush(heap,[0,K])
while heap:
    cum, node = heappop(heap)
    
    if dist[node] < cum :
        continue
    
    for next, cost in G[node]:
        if dist[next] > cum + cost :
            dist[next] = cum + cost
            heappush(heap, [dist[next], next])
for i in range(1,V+1):
    if dist[i]==INF:
        print('INF')
    else:
        print(dist[i])