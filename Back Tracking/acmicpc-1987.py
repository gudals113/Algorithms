#알파벳 백트래킹 아니면 BFS로 가능
R, C = map(int, input().split())
board = [ [] for _ in range (R)]
for i in range(R):
    line = input()
    for j in range(C):
        board[i].append( ord(line[j])-65 )


visited=[[0 for _ in range(C)] for _ in range(R)]
checklist=[0 for _ in range(26)]

checklist[board[0][0]]=1
visited[0][0]=1

tmp=1
sol=1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def DFS(x,y):
    global sol
    global tmp
    
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        
        if 0<=nx<R and 0<=ny<C :
            alphabet = board[nx][ny]
            if visited[nx][ny]==0  :
                if checklist[alphabet]==0:
                    visited[nx][ny]=1
                    checklist[alphabet]=1
                    tmp+=1
                    DFS(nx,ny)
                    tmp-=1
                    checklist[alphabet]=0
                    visited[nx][ny]=0
    
    sol = max(sol, tmp)
    return


DFS(0,0)
print(sol)




