from heapq import heappop, heappush

def solution(n, start, end, roads, traps):
    INF = float('inf')
    
    G=[ [ 0 for _ in range(n+1)] for _ in range(n+1) ]
    
    for u,v, cost in roads:
        if G[u][v] == 0 :
            G[u][v] =cost
        else:
            G[u][v] = min(G[u][v],cost)
    
    
    def dijkstra():
        heap=[]
        dist = [INF for _ in range(n+1)]        
        visited = [ [0 for _ in range(    (1<< len(traps))  )] for _ in range(1+n) ]
        dist[start]=0
        
        heappush(heap, [0,start,0])
    

        while heap:
            cost, node ,on = heappop(heap)
            
            if visited[node][on] !=0 :
                #이런 경우가 있을까?
                continue
                
            visited[node][on] = 1
                    
            #현재 노드 트랩인지, 그렇다면 켜져 있나 확인 후 상태 변경
            nowon = 0
            if node in traps :
                idx = traps.index(node)
                if 1<<idx & on == 1:
                    on &= ~(1<<idx)
                else:
                    on |= 1<<idx
                    nowon=1
            
            #현재 트랩 켜진 경우
            if nowon==1 :
                for next in range(1,n+1):
                    if next in traps and on & 1<<traps.index(next) == 1: #다음 트랩도 켜진 경우
                        if G[node][next]!=0 and visited[next][on] ==0:
                            if dist[next] >= cost + G[node][next]:
                                dist[next] = cost + G[node][next]
                                heappush(heap, [dist[next], next , on])
                                
                    else: 
                        if G[next][node]!=0 and visited[next][on] ==0:
                            if dist[next] >= cost + G[next][node]:
                                dist[next] = cost + G[next][node]
                                heappush(heap, [dist[next],next, on])
            
            #현재 트랩이 꺼진 경우 혹은 트랩이 아닌 경우             
            else:
                for next in range(1,n+1):
                    if next in traps and on & 1<<traps.index(next) == 1:
                        if G[next][node] !=0 and visited[next][on] == 0:
                            if dist[next] >= cost+ G[next][node]:
                                dist[next] = cost + G[next][node]
                                heappush(heap, [dist[next],next, on])
                                
                    else:
                        if G[node][next]!=0 and visited[next][on] ==0:
                            if dist[next] >= cost + G[node][next]:
                                dist[next] = cost + G[node][next]
                                heappush(heap, [dist[next], next , on])
        print(dist)
        return dist[end]
    
    answer = dijkstra()               
    return answer

rst =solution(4,	1	,4	,[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	,[2, 3]	)
print(rst)