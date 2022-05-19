from collections import deque


def solution(board):
    N = len(board)

    q=deque()
    visited=[[ [-1,-1]  for _ in range(N) ] for _ in range(N) ]
    
    q.append([0,0,0])
    q.append([0,0,1])
    visited[0][0] = [0,0] #세로 방향으로 방문, 가로 방향으로 방문
    
    while q:
        
        x,y,w = q.popleft()
        
        for nx,ny,nw in ([x+1,y,1],[x,y+1,0],[x-1,y,1],[x,y-1,0]):
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 : 
                newcost = 100
                if nw!=w :
                    newcost+=500
                
                if visited[nx][ny][nw] ==-1 or visited[nx][ny][nw] > visited[x][y][w] + newcost :
                    visited[nx][ny][nw] = visited[x][y][w] + newcost
                    q.append([nx,ny,nw])


    a, b =visited[N-1][N-1]
    if a==-1 or b==-1:
        answer = max(a,b)
    else:
        answer = min(a,b)
    return answer
    

solution([[0,0,0],[0,0,0],[0,0,0]])
solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]])
solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]])