##w제일 잘 풀렸다!!
from collections import defaultdict
from heapq import heappop, heappush
def solution(n, paths, gates, summits):
    INF = float('inf')
    answer =[n+2, INF]
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
    
    
    dp=[ INF for _ in range(n+1)]
    for start in gates:
        tmpanswer =-1
        visited=[0 for _ in range(n+1)]
        heap=[]
        heappush(heap,[0,start])
        


        while heap :
            minVal, node = heappop(heap)

            if dp[node] > minVal:
                dp[node]=minVal
            if minVal> tmpanswer:
                tmpanswer = minVal
            visited[node]=1
            
            #종료 조건
            if node in sumDict :
                tmpNode = node
                if answer[1] > tmpanswer or (answer[1]  == tmpanswer and answer[0] > tmpNode ):
                    answer = [tmpNode, tmpanswer]
                break

            for next, cost in G[node] :
                if not visited[next] and next not in gateDict:
                    if dp[next] >= cost :    #여기는 무조건 같아도 갈 수 있어야 봉우리 작은거 할 수 있다
                        heappush(heap, [ cost, next ])
   
    

    return answer

solution(6,[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],	[3,1],	[5])