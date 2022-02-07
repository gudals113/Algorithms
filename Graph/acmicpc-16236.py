#아기 상어 (BFS, 구현)
from collections import deque

N = int(input())
sea = [ ] # 격자 저장
# fish = [ 0 for _ in range(7)] #물고기 크기 별 마리 수 저장
shark = [] # 상어 시작 위치 저장

for i in range(N):
    line = list(map(int, input().split()))
    sea.append(line)
    for j in range(N):
        if line[j] == 9 :
            shark =[i,j]
        elif line[j] !=0 :
            pass
            # fish[ line[j] ] +=1

dx=[-1,0,0,1] #주어진 조건 순서 이건 불필요하다
dy=[0,-1,1,0]
sol = 0
size = 2
sea[shark[0]][shark[1]]=0
eaten = [0 for _ in range(8)]

#현재 기준 먹을 수 있는 물고기 위치 배열 리턴
def BFS(x,y,size):
    
    visited=[[-1 for _ in range(N)]for _ in range(N)]
    visited[x][y]=0
    
    fish=[]
    q= deque([[x,y]])
    idx = [x,y]
    while (q):
        ax, ay = q.popleft()    
        for i in range(4):
            nx, ny = ax+dx[i], ay+dy[i]
            
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==-1:
                if sea[nx][ny] <=size:
                    visited[nx][ny]=visited[ax][ay]+1
                    q.append([nx,ny])            
                    if 0<sea[nx][ny] < size :
                        fish.append([nx,ny, visited[nx][ny]])
                
        if idx==[ax,ay]: #한 바퀴 돌았을 때
            if fish!=[]: # 채워지면 종료
                return fish
            if q!=deque([]):
                idx=q[-1]
                
    return fish


while True:
    
    fish = BFS(shark[0], shark[1], size)
    if fish ==[]: # 더 이상 먹을 수 없다면 종료
        break
    
    fish.sort(key = lambda x:(x[0],x[1]))
    target = fish[0]
    sea[target[0]][target[1]]=0
    sol = sol + target[2]
    eaten[size] +=1
    
    if eaten[size]==size and size<=6:
        size+=1
    shark=target # 먹은 위치에서 다시 시작

print(sol)
