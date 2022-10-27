# kakao-internship-2022-3-2.py
# kakao-internship-2022-3.py
from heapq import heappop, heappush

INF = float('inf')
def solution(n, paths, gates, summits):
    summitsDict = {}
    gatesDict = {}
    for sm in summits:
        summitsDict[sm]=1  
    
    for gts in gates:
        gatesDict[gts]=1
        
    G = [ []for _ in range(n+1) ]
    for u,v,w in paths:
        G[u].append([v,w])
        G[v].append([u,w])

    answer =[]
    dist = [ INF for _ in range(n+1)]
    heap =[]
    
    for start in gates:
        heappush(heap,[ 0, start])
        dist[start]=0

    while heap:
        cost, node = heappop(heap)
        if dist[node]<cost:
            continue 

        if node in summitsDict:
            if len(answer)==0:
                answer=[node,cost]
                
            else:
                if answer[1] > cost:
                    answer = [node,cost]
                    
                elif answer[1] ==cost:
                    answer[0] = min(node, answer[0])
                    
            continue
        
        for next,weight in G[node]:
            if next not in gatesDict :                    
                if dist[next] > max(weight,dist[node]):
                    dist[next] = max(weight,dist[node])
                    heappush(heap,[dist[next], next])    
    return answer

solution(6,	[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]	,[1, 3]	,[5])
# solution(7	,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7]	,[1, 5])