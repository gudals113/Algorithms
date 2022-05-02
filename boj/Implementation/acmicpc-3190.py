#뱀 Dummy 
from collections import deque

N=int(input())
K=int(input())
G=[[0 for _ in range(N+1) ]for _ in range(N+1)]
for _ in range(K):
    x,y = map(int,input().split())
    G[x][y]=1   # 사과 위치는 1로 표시
L=int(input())
CD=deque([  0 for _ in range(10001) ]) # 방향 전환 최대 10001개 미리 저장 여기서 사람마다 다를듯
for _ in range(L):
    time, D = input().split()
    CD[int(time)]=D

CD.popleft() # 0초 지난 경우 미리 pop해주기
BODY = deque( [ [1,1] ])    # 꼬리 위치 저장하기

#우 하 좌 상
dx=[0,1,0,-1] 
dy=[1,0,-1,0]
dir=0 #초기 방향 설정
sol=0

x,y=1,1
while True:
    sol+=1
    x,y = x+dx[dir], y+dy[dir]
    if x<=0 or y<=0 or x>N or y>N: # 벽인 경우 종료
        break
     
    if G[x][y]==2: # 몸통인 경우 종료
        break
    
    elif G[x][y]==1:    #사과인 경우 그래프에 머리 표시 및 몸통에 저장만하기
        G[x][y]=2
        BODY.append([x,y])
        
    elif G[x][y]==0:    # 사과 아닌 경우 그래프에 머리 표시 및 몸통에 저장
        G[x][y]=2
        BODY.append([x,y])   
        
        toDelX, toDelY = BODY.popleft() # 꼬리 좌표 얻기
        G[toDelX][toDelY]=0             # 꼬리 지우기 (그래프에 표시)
        
    changeDir = CD.popleft()     # 1초 지난 상황
    if changeDir !=0:
        if changeDir=='L':
            if dir==0:
                dir=3
            else:
                dir-=1
        else :
            if dir==3:
                dir=0
            else:
                dir+=1

print(sol)