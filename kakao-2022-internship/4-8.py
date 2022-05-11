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
    
    
    dp=[ INF for _ in range(n+1)]
    for start in summits:
        tmpanswer =-1
        visited=[0 for _ in range(n+1)]
        heap=[]
        heappush(heap,[0,start])
        
        tmpNode = n+1
        tmpIntens = INF
        
        while heap :
            minVal, node = heappop(heap)
            print(node)
            if dp[node] < minVal:
                continue
            
            dp[node]=minVal
            
            if minVal> tmpanswer:
                tmpanswer = minVal
                
            visited[node]=1
            
            #종료 조건
            if node in gateDict :
                print(dp)
                tmpNode=start
                tmpIntens = tmpanswer
                break

            for next, cost in G[node] :
                if not visited[next] and next not in sumDict:
                    print(next)
                    if dp[next] > cost:    #여기는 무조건 같아도 갈 수 있어야 봉우리 작은거 할 수 있다
                        heappush(heap, [ cost, next ])
   
        if answer == []:
            answer = [tmpNode, tmpIntens]
        else:
            if answer[1] > tmpIntens or (answer[1]  == tmpIntens and answer[0] > tmpNode ):
                answer = [tmpNode, tmpIntens]

    return answer

solution(7,	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],	[1]	,[2, 3, 4])