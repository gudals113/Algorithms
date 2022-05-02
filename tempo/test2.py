def solution(h, w, n, board):
    global H, W, N
    global visited
    global G
    H, W, N = h,w,n
    answer = 0
    
    G=[ [0 for _ in range(w)] for _ in range(h) ]
    for i in range(h):
        for j in range(w):
            G[i][j] = int(board[i][j])      
    
    for i in range(h):
        for j in range(w):
            if G[i][j]==1 and visited[i][j]==0 :
                visited[i][j]=1
                tmp = DFS(i,j)
                # answer+=tmp
    return answer

def DFS(x,y):
    tmp=0#가로
    for i in range(1, N+1):
        nx, ny = x, y+1
        if nx<H and nx>=0 and ny<W and ny>=0:
            
        

    print(x,y,count)
            # 아래, 오른쪽, 대각 오른쪽 아래, 대각 왼쪽 아래
    for nx, ny in [ [x+1,y], [x,y+1], [x+1,y+1], [x+1,y-1] ]:
        if nx<H and nx>=0 and ny<W and ny>=0:
            if visited[nx][ny]==0:
                visited[nx][ny]=1
        
                if G[nx][ny]==0 and count==N:
                    
                    return 

                elif G[nx][ny]==0 and (count>N or count<N) :
                    return 
                
                elif G[nx][ny]==1 :
                    DFS(nx,ny,count+1)

            if visited[nx][ny]==1 and G[nx][ny]==0 and count==N:
                pass
                # print(nx,ny, 'here')
    
    return        

solution(7,	9,	4,	["111100000","000010011","111100011","111110011","111100011","111100010","111100000"])