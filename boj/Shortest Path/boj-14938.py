# boj-14938.py
# 서강그라운드
# sol 220915
# 데이크스트라
from collections import deque
from heapq import heappop, heappush

INF = float('inf')
N,M,R = map(int, input().split())
ITEM = [0]+list(map(int, input().split()))
G=[[] for _ in range(N+1)]
for _ in range(R):
    u,v,w = map(int, input().split())
    G[u].append([v,w])
    G[v].append([u,w])
    
answer = 0
for start in range(1,N+1):
    dist = [INF for _ in range(N+1)]
    dist[start]=0

   
    heap = [[0,start]]

    while heap:
        moved, node = heappop(heap)
        for next,cost in G[node]:
            if moved+cost<=M and dist[next] > moved+cost :
                dist[next] = moved+cost
                heappush(heap, [dist[next], next])
                
    got = 0    
    for node in range(1,N+1):
        if dist[node] != INF:
            got+=ITEM[node]
        
    answer = max(answer, got)
    
print(answer)