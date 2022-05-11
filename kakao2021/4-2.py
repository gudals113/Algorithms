def solution(n, start, end, roads, traps):
    G=[ [0 for _ in range(n+1)] for _ in range(n+1) ]
    
    for u,v, cost in roads:
        if G[u][v] == 0 :
            G[u][v] =cost
        else:
            G[u][v] = min(G[u][v],cost)
            
    
    global answer
    answer = float('inf')

    visited = [ [0 for _ in range(    (1<< len(traps))  )] for _ in range(1+n) ]
    
    def DFS(node, on, time):
        global answer 
 
        if time > answer :
            return
        
        if node == end :
            answer = min(answer,time)
            return 

        visited[node][on] = 1

        # on을 여기서 갱신해준다
        nowon = 0 #현재 온 나중에 쓰므로 저장해두기
        if node in traps :
            idx = traps.index(node)
            if 1<<idx & on == 1: #이전에 있던 곳에서 방문하기 전에 켜져 있었으면 꺼
                on &= ~(1<<idx)
            else : 
                on |= 1<<idx
                nowon=1
        
        
        if nowon==1: #현재 켜져있는 경우
      
            for next in range(1, n+1): 
                
                if next in traps and on & 1<<traps.index(next) ==1 : #현재, 다음 모두 켜진 경우
                    if G[node][next] !=0 and visited[next][on]==0:
                        DFS(next, on, time+G[node][next])
                    
                else :
                    if G[next][node] != 0 and visited[next][on]==0 : #현재만 켜져있고, 다음은 트랩이던 아니던 안켜진 경우
                        DFS(next, on, time+G[next][node])
                    
                    
        elif nowon==0: #  현재 함정이 아니거나 꺼진 경우
            
            for next in range(1, n+1):

                if next in traps and 1<<traps.index(next) & on == 1: #다음 트랩만 켜진경우
      
                    if G[next][node] != 0 and visited[next][on] == 0:
                        DFS(next, on, time+G[next][node])
                    
                else: 

                    if G[node][next] != 0  and visited[next][on] ==0:
                        DFS(next,on, time+G[node][next]) 
                        
    DFS(start, 0, 0)
    
    return answer

rst =solution(4,	1	,4	,[[1, 2, 1], [3, 2, 1], [2, 4, 1]]	,[2, 3]	)
print(rst)