# 미확인 도착지
# sol 220809
# 

# 다익스트라에서 dist 갱신하고 heappush 안해줘서 계속 틀림.
# INF = int(1e9)안해서 틀림, 질문 검색에서 참고했다.

from heapq import heappop, heappush

def deijkstra(start):
    dist = [INF for _ in range(N+1)]
    dist[start]=0
    heap =[]
    heappush(heap, [0,start])
    while heap:
        weight,node = heappop(heap)
        
        if dist[node] < weight:
            continue
        
        for next, cost in G[node]:
            if dist[next]>weight+cost:
                dist[next] = weight + cost
                heappush(heap,[dist[next],next])
    
    return dist
    
INF = int(1e9)
T= int(input())
for _ in range(T):
    N,M,K = map(int, input().split())
    s,g,h = map(int, input().split())
    
    G=[[]for _ in range(N+1)]
    
    for _ in range(M):
        u,v,w = map(int, input().split())
        if (u==g and v==h) or (u==h and v==g):
            gToh = w
        G[u].append([v,w])
        G[v].append([u,w])
        
    candidate = {}
    for _ in range(K):
        candidate[int(input())]=1

    distFromS = deijkstra(s)
    distFromG = deijkstra(g)
    distFromH = deijkstra(h)

    answer = []
    for i in candidate:
        if ( distFromS[g] + gToh + distFromH[i] == distFromS[i] ) or ( distFromS[h] + gToh+ distFromG[i] == distFromS[i] ):
            answer.append(i)
                
    answer.sort()
    print(*answer)
    
    
    
    