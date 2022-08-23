# boj-1613.py
# 역사
# 플로이드 워셜
import sys

input = sys.stdin.readline
INF = float('inf')

N, K = map(int, input().split())
dist = [ [ INF for _ in range(N+1) ] for _ in range(N+1) ]
for _ in range(K):
    u, v = map(int, input().split())
    dist[u][v]=1
    
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][j] > dist[i][k] + dist[k][j] :
                dist[i][j] = dist[i][k]+ dist[k][j]

S = int(input())
for s in range(S):
    u, v = map(int, input().split())
    if dist[u][v] == INF and dist[v][u]==INF:
        print(0)
        
    elif dist[u][v] != INF :
        print(-1)
    
    elif dist[v][u] != INF :
        print(1)