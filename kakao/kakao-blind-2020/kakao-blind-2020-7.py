# 
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def solution(board):
    answer = 0
    N = len(board)
    q = deque()
    
    visited = [[ [0,0] for _ in range(N)]for _ in range(N)]
    visited[0][1][0] = 1
    
    q.append([0,1,0,0,0,1])
    # q.append([0,0,0,1,0,1])
    while q:
        x,y,bx,by,way,time = q.popleft()
        
        #머리나 꼬리가 도착하면 종료
        if (x == N-1 and y==N-1) or (bx==N-1 and by == N-1): 
            answer = time-1
            break
        
        #뒤집기
        if visited[bx][by][way]==0:
            visited[bx][by][way] = visited[x][y][way]
            q.append([bx,by,x,y,way,time])
            
        #이동
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            nbx,nby = bx+dx[d], by+dy[d]
            if 0<=nx<N and 0<=ny<N and 0<=nbx<N and 0<=nby<N:
                if board[nbx][nby]==0 and board[nx][ny]==0 and visited[nx][ny][way] == 0 :
                    visited[nx][ny][way] = time+1
                    q.append([nx,ny,nbx,nby,way,time+1])

        #현재 가로방향
        if way==0: 

            for nx1,ny1,nx2,ny2 in ([ x+1, y, bx+1, by],[ x-1, y, bx-1,by]):
                if 0<=nx1<N and 0<=ny1<N and 0<=nx2<N and 0<=ny2<N:
                    if board[nx1][ny1]==0 and board[nx2][ny2]==0:
                        #머리 기준으로 회전
                        if visited[nx1][ny1][1] == 0:
                            visited[nx1][ny1][1] = time+1
                            q.append([nx1,ny1,x,y,1,time+1])
                            
                        #꼬리 기준으로 회전
                        if visited[nx2][ny2][1] == 0:
                            visited[nx2][ny2][1] = time+1
                            q.append([nx2,ny2,bx,by,1,time+1])

                        if visited[x][y][1] ==0 :
                            visited[x][y][1] = time+1
                            q.append([x,y,nx1,ny1,1,time+1])
                        
                        if visited[bx][by][1] == 0:
                            visited[bx][by][1] = time+1
                            q.append([bx,by,nx2,ny2,1,time+1])
                         
        elif way==1:
            for nx1,ny1,nx2,ny2 in ([x,y+1,bx,by+1],[x,y-1,bx,by-1]):
                if 0<=nx1<N and 0<=ny1<N and 0<=nx2<N and 0<=ny2<N:
                    if board[nx1][ny1]==0 and board[nx2][ny2]==0:
                        if visited[nx1][ny1][0] == 0:
                            visited[nx1][ny1][0] = time+1
                            q.append([nx1,ny1,x,y,0,time+1])
                        
                        if visited[nx2][ny2][0] == 0:
                            visited[nx2][ny2][0] = time+1
                            q.append([nx2,ny2,bx,by,0,time+1])

                        if visited[x][y][0] ==0 :
                            visited[x][y][0] = time+1
                            q.append([x,y,nx1,ny1,0,time+1])
                        
                        if visited[bx][by][0] == 0:
                            visited[bx][by][0] = time+1
                            q.append([bx,by,nx2,ny2,0,time+1])
        
    for l in visited:
        print(l)
    print(answer)
    return answer
solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])