## 비트 비교할 때 == 1이아니라 >0으로 했어야 했다..

from heapq import heappop, heappush

def solution(n, start, end, roads, traps):
    INF = float('inf')
    
    
    trapDict = {}
    for i in range(len(traps)):
        trapDict[traps[i]] = i
    
 
    G=[ [ ] for _ in range(n+1) ]
    
    for u,v, cost in roads:
        G[u].append([v,cost])
        G[v].append([u,-1*cost])

    def dijkstra():
        heap=[]
        dist = [ [INF for _ in range(    2**10  )] for _ in range(1+n) ]
        dist[start][0]=0  
        heappush(heap, [0,start,0])
        
        while heap:
            cost, node ,on = heappop(heap)
            
            if node == end:
                return cost
                
            if dist[node][on] < cost :
                continue
     
            #현재 노드 트랩인지, 그렇다면 켜져 있나 확인 후 상태 변경
            nowon = 0
            if node in trapDict :
                idx = trapDict[node]
                if  1<<idx & on  >0:
                    on &= ~(1<<idx)
                else:
                    on |= 1<<idx
                    nowon=1
            
            #현재 트랩 켜진 경우
            if nowon==1 :
                for next, weight in G[node]:
                    if next in trapDict and on & 1<<trapDict[next] >0: #다음 트랩도 켜진 경우
                        if weight>0 : #visited[next][on] ==0
                            if dist[next][on] > cost + weight:
                                dist[next][on] = cost + weight
                                heappush(heap, [dist[next][on], next , on])
                                
                    else: 
                        if weight<0 :#visited[next][on] ==0
                            if dist[next][on] > cost -weight:
                                dist[next][on] = cost -weight
                                heappush(heap, [dist[next][on],next, on])
            
            #현재 트랩이 꺼진 경우 혹은 트랩이 아닌 경우             
            else:
                for next,weight in G[node]:
                    if next in trapDict and on & 1<<trapDict[next]>0 :
                        if weight<0: # and visited[next][on] == 0
                            if dist[next][on] > cost -weight:
                                dist[next][on] = cost -weight
                                heappush(heap, [dist[next][on], next, on])
                                
                    else:
                        if weight>0 :#and visited[next][on] ==0
                            if dist[next][on] > cost + weight:
                                dist[next][on] = cost + weight
                                heappush(heap, [dist[next][on], next , on])

        
    sol = dijkstra()               
    # print(sol)
    return sol