#출발지에서 산봉우리까지만 최단 intensity로 찾기
from collections import defaultdict
from heapq import heappop, heappush
def solution(n, paths, gates, summits):
    answer =[]
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
        
        heap=[]
        heappush(heap,[0,start])
  
        while heap :
            minVal, node = heappop(heap)
            
            # if visited[node]==1:
            #     continue
            dp[node]=minVal
            visited[node]=1
            
            #종료 조건
            if node in sumDict :
                tmpNode = node
                tmpIntens = -1
                for i in range(len(dp)):
                    if i!=start and dp[i] != INF:
                        tmpIntens = max(tmpIntens, dp[i])
                break


            for next, cost in G[node] :
                if not visited[next] and next not in gateDict:

                    heappush(heap, [ cost, next ])
   
   
        if answer == []:
            answer = [tmpNode, tmpIntens]
        else:
            if answer[1] > tmpIntens:
                answer = [tmpNode, tmpIntens]
                
            if answer[1]  == tmpIntens :
                if answer[0] > tmpNode :
                    answer= [tmpNode, tmpIntens]

    return answer

