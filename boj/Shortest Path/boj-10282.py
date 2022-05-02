#해킹  다익스트라
#  V = 1만, E = 10만 (one way)
from heapq import heappop, heappush


T = int(input())
for _ in range(T):
    
    #def input()
    n,d,c = map(int, input().split())
    G=[ [] for _ in range(n+1)]
    for _ in range(d):
        a,b,s = map(int,input().split())
        G[b].append([a,s])
        
    INF = float('inf')
    heap=[]
    dist=[INF for _ in range(n+1)]
    visited=[0 for _ in range(n+1)]
    dist[c]=0
    heappush(heap, [0,c])
    
    while heap:
        cost, node = heappop(heap)
      
        if visited[node]==1:
            continue
    
        visited[node]=1
        for next, d in G[node]:
            if not visited[next]:
                if dist[next] > cost+d :
                    dist[next] = cost+d
                    
               
                    heappush(heap, [dist[next],next])
    
    count, time = 0,0
    for c in range(1, n+1):     # 방문완료된 도시의 개수 세기, 방문한 도시들 중 가장 시간이 큰 것(최단거리 중에서 최고거리)
        if visited[c] :
            count+=1
            time = max(time, dist[c])
            
    print(count, time)
    