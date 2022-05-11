from collections import deque


def solution(board):
    answer =float('inf')
    N = len(board)
    # 도착하고 나서 꼬랑지 어디로 향하나?
    # 돈 저장, 방향
    visited = [[ [-1,0] for _ in range(N) ] for _ in range(N) ]
    visited[0][0] = [0,0]
    q=deque()
    q.append([ 0,0, 0 ])
    
    while q :
        x,y,w = q.popleft()
        
        if x==N-1 and y==N-1:
            answer=min(answer,visited[x][y][0])
            
        for nx,ny,nw in (  [x+1, y, 1] , [x-1, y, 1 ], [x,y+1,2] ,[x,y-1,2]   ):
            if 0<=nx<N and 0<=ny<N and board[nx][ny]==0 :
                
                # 방향 다른경우
                if (nw==2 and w ==1) or (nw==1 and w==2):
                
                    if visited[nx][ny][0] == -1 :
                    
                    
                        visited[nx][ny][0] = visited[x][y][0] + 600
                        visited[nx][ny][1] = nw
                        q.append([nx,ny,nw])
                    
                    elif visited[nx][ny][0] >= visited[x][y][0] + 600 :
                        visited[nx][ny][0] = visited[x][y][0] + 600
                        visited[nx][ny][1] = nw
                        q.append([nx,ny,nw])
                
                elif w==0 or w==nw :
                    if visited[nx][ny][0] == -1:
                        visited[nx][ny][0] = visited[x][y][0] + 100
                        visited[nx][ny][1] = nw
                        q.append([nx,ny,nw])
                    elif visited[nx][ny][0] >= visited[x][y][0] +100 :
                        visited[nx][ny][0] = visited[x][y][0]+100
                        visited[nx][ny][1] = nw
                        q.append([nx,ny,nw])
                        
    return answer

