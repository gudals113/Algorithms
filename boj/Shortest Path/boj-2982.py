# boj-2982.py
# 국왕의 방문 dijkstra, sol 220630
from heapq import heappop, heappush

N,M = map(int, input().split())
A,B,K,G = map(int, input().split())
king = list(map(int, input().split()))
graph =  [ [] for _ in range(N+1) ]
graph2= [ [0 for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(M):
    u,v,w = map(int, input().split())
    graph[u].append([v,w])
    graph[v].append([u,w])
    graph2[u][v] = w
    graph2[v][u] = w
    
path = [ [ [-1,-1] for _ in range(N+1)] for _ in range(N+1) ]
time = 0
for i in range(1, G):
    before = king[i-1]
    node = king[i]
    path[before][node] = time, time + graph2[before][node]
    path[node][before] = time, time + graph2[before][node]
    time += graph2[before][node]

dist = [float('inf') for _ in range(N+1)]
dist[A]=K
heap = [[K,A]]

while heap:
    cost, node = heappop(heap)
    
    if dist[node] < cost :
        continue
        
    for next, weight in graph[node]:
        
        my_start= cost
        king_start, king_end = path[node][next]
        if king_start<=my_start<=king_end :
            my_start = king_end
        
        if dist[next] > my_start+weight :
            dist[next] = my_start+weight
            heappush(heap, [dist[next], next])

print(dist[B]-K)          

