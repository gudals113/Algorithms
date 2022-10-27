from collections import deque


def solution(board, r, c):
    global answer
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    answer = 30
    
    checkDict={}
    for x in range(4):
        for y in range(4):
            if board[x][y]!=0:
                checkDict[board[x][y]]=1
    all = len(checkDict)
    
    visited=[[ [0 for _ in range(7)] for _ in range(4)] for _ in range(4)]
    
    def DFS(x,y,count,tx,ty,found):
        global answer
        print(x,y,board,found,count, tx,ty ,visited[x][y][found], answer)

        if count>answer:
            return
        
        if found==(all*2)-1:
            answer = min(answer, count)
            return
        
        
        for d in range(4):
            nx,ny = x+dx[d], y+dy[d]
            if 0<=nx<4 and 0<=ny<4 and not visited[nx][ny][found]:
                
                #하나 뒤집어진 상황에서 같은 거 발견 시 둘다 없애기.
                if tx>=0 and ty>=0 and not(nx==tx and ny==ty) and board[nx][ny]==board[tx][ty]:    
                    
                    target = board[tx][ty]
                    board[nx][ny]=0
                    board[tx][ty]=0
                    visited[nx][ny][found+1]=1
                    DFS(nx,ny, count+2, -1,-1,found+1)
                    visited[nx][ny][found+1]=0
                    board[nx][ny]=target
                    board[tx][ty]=target
                
                #안 뒤집어진 상황에서 새로운거 발견시 
                elif tx<0 and ty<0 and board[nx][ny]!=0:
       
                    visited[nx][ny][found+1]=1
                    DFS(nx,ny, count+2, nx,ny,found+1)
                    visited[nx][ny][found+1]=0
                    
                #뒤집어진 상황에서 다른거 혹은 안뒤집어진 상황에서 0 발견시
                else:
  
                    visited[nx][ny][found]=1
                    DFS(nx,ny,count+1, tx,ty,found)
                    visited[nx][ny][found]=0
                    
        for d in range(4):
            idx = 0 
            while True:

                nx,ny = x+dx[d]*idx, y+dy[d]*idx
                if 0<=nx<4 and 0<=ny<4:
                    if board[nx][ny]!=0 :
                        break
                    idx+=1
                else:
                    idx-=1
                    break

            if idx==0:
                continue
            #하나 뒤집어진 상황에서 같은 거 발견 시 둘다 없애기.
            nx,ny = x+dx[d]*idx, y+dy[d]*idx
            if visited[nx][ny][found]:
                continue
            
            if tx>=0 and ty>=0 and not(nx==tx and ny==ty) and board[nx][ny]==board[tx][ty]:    
                target = board[tx][ty]
                board[nx][ny]=0
                board[tx][ty]=0
                visited[nx][ny][found+1]=1
                DFS(nx,ny, count+2, -1,-1,found+1)
                visited[nx][ny][found+1]=0
                board[nx][ny]=target
                board[tx][ty]=target
            
            #안 뒤집어진 상황에서 새로운거 발견시 
            elif tx<0 and ty<0 and board[nx][ny]!=0:
                visited[nx][ny][found+1]=1
                DFS(nx,ny, count+2, nx,ny,found+1)
                visited[nx][ny][found+1]=0
            #뒤집어진 상황에서 다른거 혹은 안뒤집어진 상황에서 0 발견시
            else:
                visited[nx][ny][found]=1
                DFS(nx,ny,count+1, tx,ty,found)
                visited[nx][ny][found]=0
                
    if board[r][c]==0:
        DFS(r,c,0,-1,-1,0)
    else:
        DFS(r,c,0,r,c,0)
        
    return answer

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0)