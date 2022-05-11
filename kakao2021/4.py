def solution(n, start, end, roads, traps):
    G=[ [0 for _ in range(n+1)] for _ in range(n+1) ]
    
    for u,v, cost in roads:
        G[u][v] = cost
    
    # 1 << len(traps)
    #traps =[2,5,10]
    
    global answer
    answer = float('inf')
    
    visited =  [[0,0] for _ in range(n+1)]  
    
    def DFS(node, on, time):
        global answer 

        if time > answer :
            return
        
        if node == end :
            answer = min(answer,time)
            return 
        
        
        if node in on :
            visited[node][1] = 1
        else:
            visited[node][0] = 1
        
        #현재 노드가 켜져 있지 않다면!!
        if node not in on :
            for next in range(1,n+1):
                
                #만약 다음 노드가 켜진 트랩이라면 (하나만 켜짐)
                if next in on :
                    if G[next][node] !=0 and not visited[next][0] :
                        new = on[:]
                        new.remove(next)
                        DFS(next, new, time+G[next][node])
            
                #만약 다음 노드가 트랩이지만 꺼져있다면 (둘다 꺼짐)
                elif next in traps:
                    if G[node][next] !=0 and not visited[next][1]:
                        new = on[:]
                        new.append(next)
                        DFS(next,new, time+G[node][next])
                    
                    
                #만약 다음 노드가 트랩이 아니라면 (둘다 꺼짐)
                else:        
                    if G[node][next] != 0 and not visited[next][0]:
                        DFS(next, on, time+G[node][next])
        
        
        
        
        #현재 노드가 켜져 있다면!!
        else :
            for next in range(1,n+1):
    
                #만약 다음 노드가 켜진 트랩이라면 (둘다 켜짐)
                if next in on :
                    if G[node][next] !=0 and not visited[next][0]: #그럼 가면 꺼진다
                        new = on[:]
                        new.remove(next)
                        DFS(next, new, time+G[node][next])
            
                #만약 다음 노드가 트랩이지만 꺼져있다면 (하나만 켜짐)
                elif next in traps:
                    if G[next][node] !=0 and not visited[next][1]:
                        new = on[:]
                        new.append(next)
                        DFS(next,new, time+G[next][node])
                    
                    
                #만약 다음 노드가 트랩이 아니라면 (둘다 꺼짐)
                else:        
                    if G[next][node] != 0 and not visited[next][0]:
                        DFS(next, on, time+G[next][node])
                
                

     
    DFS(start, [], 0)
    
    return answer


# rst  =solution(3,	1	,3,	[[1, 2, 2], [3, 2, 3]],	[2])
rst = solution(4,	1,	4	,[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	,[2, 3])
print(rst)