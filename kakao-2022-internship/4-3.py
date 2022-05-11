#출발지에서 산봉우리까지만 최단 intensity로 찾기

#왜 이전꺼 보다 안되냐
from collections import defaultdict
from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    answer =[]
    INF = float('inf')
    G=[[]for _ in range(n+1)]
    for u,v,w in paths:
        G[u].append([v,w])
        G[v].append([u,w])
    gateDict = defaultdict(int)
    for g in gates:
        gateDict[g] =1
    sumDict = defaultdict(int)
    for s in summits:
        sumDict[s] = 1

    def find(start):
        visited=[0 for _ in range(n+1)]
        
        #출발점에서 노드까지 최소 가중치
        dp=[ INF for _ in range(n+1)]
        
        heap=[]
        heappush(heap,[0,start])
  
        while heap :
            minVal, node = heappop(heap)
            
  
            dp[node]=minVal
            visited[node]=1
            
            #종료 조건
            if node in sumDict :    
                return node, dp


            for next, cost in G[node] :
                if not visited[next] and next not in gateDict:

                    heappush(heap, [ cost, next ])
            
        
    for start in gates:
        node, dp = find(start)
        ints = -1
        for i in range(len(dp)):
            if i!=start and dp[i] != INF:
                ints = max(ints, dp[i])       
                
        if len(answer)==0:
            answer.append(node)
            answer.append(ints)
            
        else:
            if answer[1] > ints or ( answer[1]  == ints and answer[0] > node) :
                answer = [node, ints]
            
    return answer

