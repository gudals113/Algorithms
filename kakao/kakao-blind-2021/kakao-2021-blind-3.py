# kakao-2021-blind-3.py
def solution(n, s, a, b, fares):
    answer = 0
    G = [[0 for _ in range(n+1)]for _ in range(n+1)]
    dist = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for u,v,w in fares:
        G[u][v]=w
        G[v][u]=w
        dist[u][v] = w
        dist[v][u] = w
        dist[u][u] = 0
        dist[v][v] = 0
    
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if dist[i][j] > dist[i][k]+ dist[k][j]:
                    dist[i][j] = dist[i][k]+ dist[k][j]
    answer = dist[s][a] + dist[s][b]
    for together in range(1,n+1):
        answer = min(answer, dist[s][together]+ dist[together][a] + dist[together][b])
        
    print(answer)
    return answer
solution(6,	4,	6,	2	,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])

solution(7,	3	,4	,1	,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]	)