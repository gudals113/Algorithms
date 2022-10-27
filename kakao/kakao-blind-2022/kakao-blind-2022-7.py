def solution(board, aloc, bloc):
    if aloc==bloc:
        return 1
    global answer
    answer = float('inf')
    N = len(board)
    M = len(board[0])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    visited =[ [ 0 for _ in range(M)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if board[x][y]==0:
                visited[x][y]=1
    
    def DFS(ax,ay,bx,by,count):
        global answer
        an = []
        bn = []
        print(ax,ay,bx,by,count)
        
        if ax==bx and ay == by:
            answer = min(answer,count+1)
        
        for d in range(4):
            nax,nay = ax+dx[d], ay+dy[d] 
            nbx,nby = bx+dx[d], by+dy[d]
            
            if 0<=nax<N and 0<=nay<N and not visited[nax][nay]:
                an.append([nax,nay])
            if 0<=nbx<N and 0<=nby<N and not visited[nbx][nby]:
                bn.append([nbx,nby])
        
            
        for nax,nay in an:
            for nbx,nby in bn:
                
                visited[nax][nay]=1
                visited[nbx][nby]=1
                DFS(nax,nay, nbx,nby,count+2)
                visited[nax][nay]=0
                visited[nbx][nby]=0
    
    visited[aloc[0]][aloc[1]], visited[bloc[0]][bloc[1]]=1,1
    DFS(aloc[0],aloc[1],bloc[0],bloc[1],0)    
    
    print(answer)
    return answer

solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]	,[1, 0],	[1, 2])