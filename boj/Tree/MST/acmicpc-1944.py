#복제 로봇 크루스칼 알고리즘 
from collections import deque

def find(u) :
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return
    p[u]=v

N, M = map(int, input().split())
G=[[0 for _ in range(N)]for _ in range(N)]
keyidx=0
# keyidx=1
K=[] 

for i in range(N):
    line = input()
    for j in range(N):
        word = line[j]
        if word == 'S' or word=='K':
            K.append([keyidx, i, j])
            G[i][j]=keyidx+10 
            keyidx+=1
            
        # if word == 'S':       #k idx=1로 시작하고 S,K 나눠서 이렇게 하면 틀리는 이유가 뭘까
        #     K.append([0,i,j])
        #     G[i][j]= 10        #그래프에는 시작 지점은 10으로 저장

        # elif word=='K':
        #     K.append([keyidx,i,j])
        #     G[i][j]=keyidx+10   #그래프에는 key는 keyidx + 10 저장
        #     keyidx+=1
            
        else:
            G[i][j]=int(word)
E=[]
def BFS(idx):
    global E
    startx, starty = K[idx][1], K[idx][2]
    
    visited=[ [-1 for _ in range(N)]for _ in range(N) ]
    
    visited[startx][starty]=0
    
    q=deque([[startx,starty]])
    
    while q:
        x,y = q.popleft()
        
        for nx,ny in [ [x,y+1],[x,y-1],[x+1,y],[x-1,y] ] :
            if nx>=0 and nx<N and ny>=0 and ny<N:     
            
                if visited[nx][ny]==-1 and G[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
                    
                    if G[nx][ny]!=0:    
                        E.append([visited[nx][ny], idx, G[nx][ny]-10 ]) # 거리, 시작점, 끝점


connected = [0 for _ in range(M+1)]
connected[0]=1

for i in range(M+1):
    BFS(K[i][0])        
E.sort(key=lambda x : x[0])

p=[-1 for _ in range(M+1)]
count =0
sol=0
for i in range(len(E)):
    if count==M: #s까지 합치면 M+1개
        break
    cost, start, end = E[i]
    if find(start) != find(end):
        if connected[start]<3 and connected[end]<3:         #이조건 없어도 맞는거 보면 뭔가 테케가 부족한거 아닌가 싶다
            connected[start]+=1
            connected[end]+=1
        sol  +=  cost
        count += 1
        union(start, end)
if count == M:
    print(sol)
else:
    print(-1)
