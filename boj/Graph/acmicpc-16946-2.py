#벽 부수고 이동하기 4 (visited에 저장)
from collections import deque
 
N, M = map(int,input().split())
G=[ [0 for _ in range(M)] for _ in range(N)]
SOL= [[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(M):
        G[i][j] = int(l[j])
    
#visited애 0 개수 역추적해서 저장 / union find해서 저장
visited=[ [0 for _ in range(M)]for _ in range(N) ] 

def countBFS(idx):
    x,y = idx//M, idx%M
    q=deque([ [x,y] ])
    t=[ [idx, x,y] ]
    count=1
    while q:
        x,y = q.popleft()
        
        for nx,ny in [ [x+1,y], [x-1,y], [x,y+1], [x,y-1] ] :
            if nx>=0 and nx<N and ny>=0 and ny<M :
                if G[nx][ny]==0:
                    if visited[nx][ny]==0:
                        
                        visited[nx][ny]=1
                        count+=1
                        t.append([idx, nx,ny]) # 벽 있어도 연결된 경우 중복 반영하지 않도록 bfs 시작 idx 저장
                        q.append([nx,ny])
    
    #가장 마지막에 추가된 방문 정보
    while t:
        idx, x,y = t.pop()
        visited[x][y]=[count,idx]
                            
def solBFS(idx):
    sol=1
    candidate=[]
    x,y = idx//M, idx%M
    for nx,ny in [ [x+1,y], [x-1,y], [x,y+1], [x,y-1] ] :
        if nx>=0 and nx<N and ny>=0 and ny<M :
            if G[nx][ny]==0:
                num, idx = visited[nx][ny]
                if idx not in candidate:
                    candidate.append(idx)
                    sol+=num 
    return sol
   
                
for i in range(N*M):
    x,y = i//M, i%M
    if G[x][y]==0 and visited[x][y] ==0:
        visited[x][y]=1
        countBFS(i) 
        

for i in range(N*M):
    x,y = i//M, i%M
    if G[x][y]==1 and visited[x][y]==0:
        visited[x][y]=1
        SOL[x][y] = solBFS(i) %10
            
for i in range(N):
    for j in range(M):
        print(SOL[i][j],end='')
    print()