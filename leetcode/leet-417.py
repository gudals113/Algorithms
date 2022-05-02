from collections import deque
def pacificAtlantic(heights):
        M = len(heights)
        N = len(heights[0])
        
        PO= [ [0 for _ in range(N)] for _ in range(M)]
        AO= [ [0 for _ in range(N)] for _ in range(M)]
        
        
        def BFS(x,y,ocean):
            visited=[ [0 for _ in range(N)] for _ in range(M)]
            q= deque([[x,y]])
            
            while q:
                x,y = q.popleft()
                # print(x,y)
                
                for nx,ny in ([x,y+1], [x,y-1], [x+1,y],[x-1,y]):
                    if 0<=nx<M and 0<=ny<N and not visited[nx][ny]:
                        if (x <0 or y<0 or x==M or y==N) or heights[nx][ny] >= heights[x][y]:
                            if ocean=='P':
                                PO[nx][ny]=1
                            else:
                                AO[nx][ny]=1
                                
                            visited[nx][ny]=1
                            q.append([nx,ny])
            
            
        for i in range(M):
            BFS(i,-1,'P')
            BFS(i,N,'A')
        for j in range(N):
            BFS(-1,j,'P')
            BFS(M,j,'A')
         
        sol=[]
        for i in range(M):
            for j in range(N):
                if PO[i][j]==1 and AO[i][j]==1:
                    sol.append([i,j])
        return sol
        # print(sol)
        
