# kakao-internship-2022-3.py
# 모든 시작점에 대하여 다익스트라 돌리면 당연히 시간초과가 발생한다.
# 이것을 알고 있으면, 이렇게 풀면 안된다. 당연히. 슬쩍 밀어넣을 생각하지 말자 시간 부족하다.

from heapq import heappop, heappush


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
    #힙에 시작점 넣기
    maxIntentsity = float('inf')

    for start in gates:
        visited = [ 0 for _ in range(n+1)]
        heap =[]
        heappush(heap,[0,start])
        intensity = -1
        while heap:
            
            dist, node = heappop(heap)
            
            if visited[node] or dist > maxIntentsity:
                continue

            visited[node]=1
            intensity = max(intensity, dist)
            
            if summitsDict.get(node)!=None :
                if len(answer)==0:
                    answer=[node,intensity]
                    maxIntentsity = intensity
                else:
                    if answer[1] > intensity:
                        answer = [node,intensity]
                        maxIntentsity = intensity
                    elif answer[1] == intensity:
                        answer[0] = min(node, answer[0])
                break
            
            for next,weight in G[node]:
                if gatesDict.get(next)==None and not visited[next]:                    
                        heappush(heap,[weight,next])
    

    return answer

solution(7	,[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],	[3, 7]	,[1, 5])