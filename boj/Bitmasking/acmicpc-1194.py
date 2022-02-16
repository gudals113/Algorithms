#달이 차오른다 가자 bitmasking
from collections import deque
N,M= map(int, input().split())
miro=[]

for i in range(N):
    line = input()
    miro.append(line)
    if '0' in line:
        startx=i
        starty=line.find('0')

visited=[[[0 for _ in range(64)] for _ in range(M)]for _ in range(N)] #visited[x][y] x=세로N, y=가로M
visited[startx][starty][0]=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]

keylist=['a', 'b', 'c', 'd', 'e', 'f']
doorlist=['A', 'B', 'C', 'D', 'E', 'F']
sol=float('inf')

def BFS(ax, ay, akey, acost): #넣기 전에 잘 생각하고 넣고 방문처리하기, 처음 좌표 방문처리하기
    global sol
    tmp=1
    q=deque([[ax,ay,akey, acost]])

    while(q):
        x,y,key,cost=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
    
            if 0<=nx<N and 0<=ny<M and visited[nx][ny][key] != 1 and miro[nx][ny]!='#':
                
                if miro[nx][ny] in doorlist :
                    door=miro[nx][ny]
                    need=chr( ord(door)+32 ) #필요한 key 문자열
                    if key & 1<<keylist.index(need) !=0:
                        visited[nx][ny][key] = 1
                        q.append([nx,ny,key, cost+1])    

                elif miro[nx][ny] in keylist :
                    get = miro[nx][ny] #key 문자열
                    newkey= key | 1<<keylist.index(get)
                    visited[nx][ny][newkey] = 1
                    q.append([nx,ny,newkey,cost+1])
                    
                elif miro[nx][ny] =='.' or miro[nx][ny]=='0':
                    visited[nx][ny][key] = 1
                    q.append([nx,ny,key,cost+1])
                    
                elif miro[nx][ny] =='1':
                    sol=min(sol,cost+1)
                
                    
BFS(startx,starty, 0,0)
if sol==float('inf'):
    print(-1)
else:
    print(sol)