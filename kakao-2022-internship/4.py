#출발지에서 산봉우리까지만 최단 intensity로 찾기
from collections import defaultdict, deque
from heapq import heappop, heappush


def solution(n, paths, gates, summits):
    INF = float('inf')
    G=[[]for _ in range(n+1)]
    for u,v,w in paths:
        G[u].append([v,w])
        G[v].append([u,w])
    
    #출발점
    gateDict = defaultdict(int)
    for g in gates:
        gateDict[g] =1
    sumDict = defaultdict(int)
    for s in summits:
        sumDict[s] = 1
    
    
    for start in gates:
        visited=[0 for _ in range(n+1)]
        
        #출발점에서 노드까지 최소 가중치
        dp=[ INF for _ in range(n+1)]
        
        heappush(heap,[0,start])
        heap=[]
        visited[start] =1
        
        while heap :
            minVal, node = heappop(heap)
            
            if node in sumDict :
                print(dp,node)
                #산봉우리 도착하면 dp에서 최댓값 뽑아
                break
            
            if dp[node] < minVal :
                continue
            
            visited[node]=1
            
            for next, cost in G[node] :
                if not visited[next] and next not in gateDict:
                    
                    if cost > dp[next] or dp[next]==INF:
                        dp[next] = cost
                    
                    heappush(heap, [ dp[next], next ])
        

    
    answer = []
    return answer

solution(6,
         [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
         [1, 3],
         [5]	)