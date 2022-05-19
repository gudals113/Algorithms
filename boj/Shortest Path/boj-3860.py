#할로윈 묘지 #벨만 포드 

        #1 다익스트라로 풀기 불가능하다. 음의 거리가 있다.
        #2 벨만 포드. -> sol
        #3 BFS로 갱신하면서 진행 

#2    
from collections import deque


answer=[]
INF = float('inf')
while True:
    W, H = map(int,input().split())
    if W==0 and H==0:
        break
    
    G = int(input())
    
    graph = [ [0 for _ in range(H)]for _ in range(W) ]
    hole=[[INF,INF,INF]]
    for _ in range(G):
        x,y = map(int,input().split())
        graph[x][y] = -1
    
    E = int(input())
    for i in range(1,E+1):
        x,y, hx,hy, t = map(int,input().split())    
        graph[x][y] = i
        hole.append([hx,hy,t])
    
    
    # def check(a,b):
    #     q=deque([ [a,b] ])
    #     visited= [[0 for _ in range(H)] for _ in range(W)]
    #     visited[a][b]=1
    #     while q:
    #         x,y = q.popleft()
    #         if x==W-1 and y==H-1:
    #             return True
    #         for nx,ny in ([x,y+1], [x,y-1], [x+1,y], [x-1,y]):
    #             if 0<=nx<W and 0<=ny<H and visited[nx][ny]==0 :
    #                 q.append([nx,ny])
    #                 visited[nx][ny]=1
            
    #     return False
    
    
    
    dist = [ [INF for _ in range(H)] for _ in range(W) ]
    dist[0][0]=0
    def bf():
        for count in range(H*W):
            for x in range(W):
                for y in range(H):
                    
                    if x==W-1 and y==H-1 or graph[x][y]==-1:
                        continue
                    
                    
                    elif graph[x][y] >=1:
                        outX,outY,outTime = hole[ graph[x][y] ]
                        if dist[outX][outY] > dist[x][y] + outTime :
                            dist[outX][outY] = dist[x][y] + outTime 

                            if count == H*W-1 :
                                return float('-inf')

                          
                    elif graph[x][y]==0:
                        for nx,ny in ([x,y+1], [x,y-1], [x+1,y], [x-1,y]):
                            if 0<=nx<W and 0<=ny<H : 
                                if graph[nx][ny] >=0 :
                                    if dist[nx][ny] > dist[x][y]+1:
                                        dist[nx][ny] = dist[x][y]+1
                                        
                                        if count == H*W-1:
                                            return float('-inf')
                                            # if check(nx,ny):
                                            #     return False
                                   
        return dist[W-1][H-1]
    
    result = bf()
    if result == INF:
        print('Impossible')
    elif result == float('-inf') :
        print('Never')
    else:
        print(result)                    
        
# for i in range(len(answer)):
#     print(answer[i])
    
    
