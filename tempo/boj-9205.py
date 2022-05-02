T = int(input())
INF = float('inf')


for _ in range(T):
    N = int(input())
    G=[] #0 집, 1 - N 편의점, 락페스티벌 장소
    for _ in range(N+2):
       G.append(list(map(int,input().split())))
       
    dist = [[INF for _ in range(N+2)]for _ in range(N+2)]
    for i in range(N+2):
        for j in range(N+2):
            tmp = abs(G[i][0] - G[j][0]) + abs(G[i][1]-G[j][1])
            if tmp<=1000:
                dist[i][j]=tmp
    
    
    for k in range(N+2):
        for i in range(N+2):
            for j in range(N+2):
                if dist[i][j] > dist[i][k] + dist[k][j] :
                    dist[i][j] = dist[i][k] + dist[k][j]

    if dist[0][N+1]==INF:
        print('sad')
    else:
        print('happy')