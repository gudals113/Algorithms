#토마토
from collections import deque
M,N,H = map(int, input().split())
tomato = []
already =[] #이미 익은 좌표
notready = 0 #인 익은 개수
for i in range(H):
    floor = []
    for j in range(N):
        
        line = list(map(int, input().split()))
        
        floor.append( line )
        
        for k in range(M):
            if line[k] == 1:
                already.append([i,j,k])
            elif line[k] == 0:
                notready+=1
        
    tomato.append(floor)

visited=[[ [0 for _ in range(M)] for _ in range(N) ] for _ in range(H)]
dx,dy,dh= [0,0,1,-1,0,0], [1,-1,0,0,0,0], [0,0,0,0,1,-1]

def BFS():
    global notready
    q=deque([])
    
    for tom in already:
        h,x,y = tom[0],tom[1],tom[2]
        visited[h][x][y]=1
        q.append(tom)
    
    tmp=0
    if q !=deque([]):
        idx =q[-1]
    
    while (q):
       
        h,x,y = q.popleft()
            
        for i in range(6):
            nH,nX,nY = h+dh[i], x+dx[i], y+dy[i]
            
            if 0<=nH<H and 0<=nX<N and 0<=nY<M :    
                if visited[nH][nX][nY]==0 and tomato[nH][nX][nY]==0:
                    visited[nH][nX][nY]=1
                    tomato[nH][nX][nY]=1
                    notready-=1
                    q.append([nH,nX,nY])
        
        if [h,x,y] == idx:
            tmp+=1
            if q !=deque([]):
                idx = q[-1]
            
    return tmp
            
                    
if notready==0:
    print(0)
else:
    sol = BFS()
    if notready>0:  
        print(-1)
    else:
        print(sol-1)