import sys
input = sys.stdin.readline

N,M = map(int,input().split())
INF = float('inf')

dist=[ [INF for _ in range(N+1)]for _ in range(N+1)]

for _ in range(M):
    u,v,b = map(int,input().split())

    if b == 1: #양방향 길
        dist[u][v]=0
        dist[v][u]=0
    else:      #one way
        dist[u][v]=0
        dist[v][u]=1        

#제자리 걸음 초기화
for i in range(1,N+1):
    dist[i][i]=0
       
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

K = int(input())
for i in range(K):
    u,v = map(int,input().split())
    print(dist[u][v])