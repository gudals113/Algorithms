#구슬 탈출2 BFS, hint 220603
from collections import deque

N,M = map(int, input().split())
G=[['.' for i in range(M)]for _ in range(N)]
R, B=[], []
for i in range(N):
    line = input()
    for j in range(M):
        
        if line[j]=='#' or line[j]=='O':
            G[i][j]=line[j]
        
        elif line[j]=='B':
            B=[i,j]
            
        elif line[j]=='R':
            R = [i,j]

dir = [[0,1],[1,0],[0,-1],[-1,0]]

def move(x,y,idx) :
    dx,dy = dir[idx]
    nx,ny = x,y
    count=0
    
    while True:
        nx,ny = nx+dx, ny+dy
        count+=1
        if G[nx][ny]=='.':
            continue
        
        elif G[nx][ny]=='O':
            break
        
        else: 
            nx-=dx
            ny-=dy
            count-=1
            break
               
    return nx,ny,count

q=deque()   
q.append([R[0],R[1],B[0],B[1],0])

sol = 11
while q:
    rx,ry,bx,by,time = q.popleft()

    if time>=sol:
        continue
    
    for i in range(4):
        dx,dy = dir[i]
        bbx, bby, bcount = move(bx,by,i)
        rrx, rry, rcount = move(rx,ry,i)
        
        if G[bbx][bby]=='O':           
            continue 
        
        elif G[rrx][rry]=='O':
            sol = min(sol, time+1)

        elif bbx==rrx and bby==rry:  
            if bcount>rcount:
                q.append([rrx,rry,bbx-dx,bby-dy,time+1])
            else:
                q.append([rrx-dx,rry-dy,bbx,bby,time+1])
        else:
            q.append([rrx,rry,bbx,bby,time+1]) 
            
if sol==11:
    print(-1)
else:
    print(sol)