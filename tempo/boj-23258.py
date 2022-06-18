#밤편지 #220510 - 
from heapq import heappush

N,Q = map(int,input().split())
G = [[]]
for _ in range(N):
    G.append([0]+list(map(int, input().split())))
INF = float('inf')
dist = [ [[INF for _ in range(N+1)] for _ in range(N+1) ]for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if G[i][j] !=0 :
            dist[i][j][0] = G[i][j]


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][j][k-1] > dist[i][k][k-1] + dist[k][j][k-1] :
                dist[i][j][k]  = dist[i][k][k-1] + dist[k][j][k-1] 
