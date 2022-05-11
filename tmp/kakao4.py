def solution(board):
    N = len(board)
    global answer
    answer = float('inf')
    
    def DFS(x,y, before, cost):
        global answer
        
        if cost>=answer:
            return
        
        if x==N-1 and y==N-1:
            answer = cost
            # print(visited)
            return

        for nx,ny,w in ([x+1,y,1],[x,y+1,2],[x-1,y,1],[x,y-1,2]):
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 and visited[nx][ny]==0:
                new = cost+100
                if (before == 1 and w==2) or (before==2 and w==1):
                    new+=500
                
                visited[nx][ny]=1
                DFS(nx,ny,w, new)
                visited[nx][ny]=0


    visited=[ [0 for _ in range(N)] for _ in range(N)]
    visited[0][0]=1
    DFS(0,0,0,0)
    print(answer)
    return answer

# solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
# solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])
# solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]])
# 