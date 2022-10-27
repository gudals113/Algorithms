from copy import deepcopy
from heapq import heappop, heappush
import sys
sys.setrecursionlimit(10**5)

def solution(board, r, c):
    global answer
    answer = float('inf')
    card={}
    startPoint = []
    for x in range(4):
        for y in range(4):
            carNum = board[x][y]
            if carNum!=0:
                if carNum in card:
                    card[carNum].append([x,y])
                else:
                    card[carNum] = [[x,y]]
                startPoint.append([x,y])

    INF = float('inf')
    dx,dy = [0,0,1,-1],[1,-1,0,0]
    def findPath(board, x,y, targetX, targetY):
        heap = [[0,x,y]]
        dist = [[INF for _ in range(4)] for _ in range(4)]
        dist[x][y] = 0
        while heap:
            cost, x,y = heappop(heap)
            
            if dist[x][y] < cost:
                continue
            
            if x==targetX and y==targetY:
                return cost
            
            for d in range(4):
                nx,ny = x+dx[d], y+dy[d]
                if 0<=nx<4 and 0<=ny<4 and dist[nx][ny] > cost+1 :
                    dist[nx][ny]=cost+1
                    heappush(heap, [cost+1,nx,ny])

            for d in range(4):
                idx = 1
                while True:
                    nx,ny = x+dx[d]*idx, y+dy[d]*idx
                    if 0<=nx<4 and 0<=ny<4:
                        if board[nx][ny]!=0 :
                            break
                        idx+=1
                    else:
                        idx-=1
                        break
                nx,ny = x+dx[d]*idx, y+dy[d]*idx
                if idx==0:
                    continue
                if dist[nx][ny] > cost+1 :
                    dist[nx][ny] = cost+1
                    heappush(heap, [cost+1,nx,ny])
                    
    visited = [[0 for _ in range(4)] for _ in range(4)]    
    def DFS(board,count,x,y,found):
        global answer
        # print(board,x,y,'count:',count,'found:', found)
        
        if count>answer:
            return
        
        if found== len(card):
            answer = min(answer,count)

        num = board[x][y]
        if num==0:
            for i in range(len(startPoint)):
                sx,sy = startPoint[i]
                if not visited[sx][sy]:
                    cost = findPath(board,x,y,sx,sy)
                    visited[sx][sy]=1
                    DFS(board,cost+count+1,sx,sy,found)
                    visited[sx][sy]=0
                    
        elif num!=0:
            newBoard = deepcopy(board)
            cardList=card[num]
            
            if cardList[0]==[x,y]:
                tx,ty = cardList[1]
            else:
                tx,ty = cardList[0]
            
            visited[tx][ty]=1
            newBoard[tx][ty]=0
            newBoard[x][y]=0
            cost = findPath(board,x,y,tx,ty)
            DFS(newBoard,count+cost+1,tx,ty,found+1)
            visited[tx][ty]=0


    if board[r][c]==0:
        DFS(board,0,r,c,0)
    else:
        DFS(board,1,r,c,0)
        
    print(answer)
    return answer

solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],	1,	0)
solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]],	0	,1)