N = int(input())
M = int(input())
INF = float('inf')
dist = [ [INF for _ in range(N+1)]for _ in range(N+1) ]
for _ in range(M):
    a,b,c = map(int,input().split())
    dist[a][b]= min(dist[a][b], c)
    
for k in range(1, N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            
            if i==j:
                dist[i][j]=0
                
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k]+ dist[k][j]


for i in range(1,N+1):
    for j in range(1,N+1):
        if dist[i][j]==INF:
            print(0, end=' ')
        else: 
            print(dist[i][j],end=' ')
    print()
