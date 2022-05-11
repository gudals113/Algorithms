#출발지에서 산봉우리까지만 최단 intensity로 찾기


##w제일 잘 풀렸다!!
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
        dp=[ INF for _ in range(n+1)]
        heap=[]
        heappush(heap,[0,start])
        tmpNode = n+1
        tmpIntens = INF
        
        while heap :
            minVal, node = heappop(heap)
        
            if dp[node] < minVal:
                continue
            
            dp[node]=minVal
            visited[node]=1
            
            #종료 조건
            if node in sumDict :
                tmpNode = node
                tmpIntens = -1
                for i in range(len(dp)):
                    if i!=start and dp[i] != INF and dp[i]>tmpIntens:
                        tmpIntens = dp[i]
                break

            for next, cost in G[node] :
                if not visited[next] and next not in gateDict:
                    if dp[next] > cost:
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

rst =solution(6,
         [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
         [1, 3],
         [5]	)
print(rst)
# solution(5,	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]]	,[1, 2]	,[5])