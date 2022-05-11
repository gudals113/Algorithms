#출발지에서 산봉우리까지만 최단 intensity로 찾기
from collections import defaultdict
from heapq import heappop, heappush
from tabnanny import check
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
    checkDict=defaultdict(int)
    startDict=defaultdict(int)
    
    visited=[[0 for _ in range(len(gates)) ] for _ in range(n+1)]
    dp=[ [INF for _ in range(len(gates))] for _ in range(n+1)]
    heap=[]
    for i in range(len(gates)):

        startDict[gates[i]] = i
        heappush(heap,[0, gates[i], startDict[i]])

    # print(heap)
    
    
    
    tmpNode = n+1
    tmpIntens = INF
    while heap :
        minVal, node, startNode = heappop(heap)

        if dp[node][startNode] < minVal:
            continue
        
        dp[node][startNode]=minVal
        visited[node][startNode]=1
        
        #종료 조건
        if node in sumDict and startNode not in checkDict:
            checkDict[startNode]=1
            tmpNode = node
            tmpIntens = -1
            for i in range(len(dp)):
                if dp[i][startNode]!=0 and dp[i][startNode] != INF and dp[i][startNode]>tmpIntens:
                    tmpIntens = dp[i][startNode]
            
            if answer == []:
                answer = [tmpNode, tmpIntens]
            else:
                if answer[1] > tmpIntens:
                    answer = [tmpNode, tmpIntens]
                    
                if answer[1]  == tmpIntens :
                    if answer[0] > tmpNode :
                        answer= [tmpNode, tmpIntens]
                    
            continue
        
        for next, cost in G[node] :
            if not visited[next][startNode] and next not in gateDict:
                if dp[next][startNode] > cost:
                    heappush(heap, [ cost, next, startNode ])

    
    return answer

rst =solution(6,
         [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
         [1, 3],
         [5]	)
print(rst)
# solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]	,[1, 2]	,[5])