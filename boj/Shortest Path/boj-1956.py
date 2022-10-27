#운동장
# sol 220830
# 플로이드 워셜

V, E = map(int, input().split())
INF = float('inf')
dist  = [ [ INF for _ in range(V+1)]for _ in range(V+1)]
for _ in range(E):
    u,v, c= map(int, input().split())
    dist[u][v]=c

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if dist[i][j] > dist[i][k]+dist[k][j]:
                dist[i][j] = dist[i][k]+dist[k][j]
                
answer = INF             
for i in range(1,V+1):
    answer = min(answer, dist[i][i])
if answer == INF:
    answer = -1

print(answer)