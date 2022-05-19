#저울, 플로이드 워셜, sol220513
INF = float('inf')
N = int(input())
M = int(input())
dist = [ [INF for _ in range(N+1)] for _ in range(N+1) ]
for _ in range(M):
    u, v = map(int,input().split())
    dist[v][u] = 1
    
    
for k in range(1,N+1):
    dist[k][k] = 0
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

sol = [0 for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        if dist[i][j] == INF and dist[j][i]==INF:
            sol[i]+=1

for i in range(1,N+1):
    print(sol[i])
            