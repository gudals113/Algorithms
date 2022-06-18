from heapq import heappop, heappush

INF = float('inf')
T = int(input())
for _ in range(T):
    N,M,K = map(int,input().split())
    
    #다른 다익스트라와 다른 점은 비용의 한계가 있다 - > 비용의 한게 만큼 dist 배열 추가
    #시간 기준으로 최단거리
    G=[[]for _ in range(N+1)]
    for _ in range(K):
        u,v,c,d = map(int,input().split())
        G[u].append([v,c,d])
        
    
    dist = [ [INF for _ in range(M+1)] for _ in range(N+1) ]
    heap = []
    dist[1] = [0 for _ in range(M+1)]
    heappush(heap, [0,1,0])
    
    while heap:
        
        saveTime, node, saveCost = heappop(heap)
        
        if saveTime > dist[node][saveCost] or saveCost > M:
            continue
        
        # if node == N :
        #     break
        
        for next, cost, time in G[node]:
            if saveCost+cost<=M and dist[next][saveCost+cost] > saveTime + time:
                dist[next][saveCost+cost] = saveTime + time
                heappush(heap, [saveTime + time, next, saveCost+cost])
    
    answer = INF
    for i in range(M+1):
        answer = min(dist[N][i], answer)
        
    if answer==INF:
        print('Poor KCM')
    else:
        print(answer)
    
    
    
# 다익스트라 문제인데 왜 메모리 초과가 발생할까? 
# heappush하는 부분에서 너무 많이 집어 넣고 있나?
# 체크 해보자!