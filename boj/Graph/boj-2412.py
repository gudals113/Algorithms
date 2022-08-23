# boj-2412.py
#2412번 암벽 등반 다익스트라, BFS , sol 220701
from collections import deque
from heapq import heappop, heappush
N,T = map(int, input().split())
G={0:{0:1}}
dist={0:{0:float('inf')}}
for _ in range(N):
    x,y = (map(int,input().split()))
    if x in G:
        G[x][y]=1
        dist[x][y]=float('inf')
    else:
        G[x]={y:1}
        dist[x]={y:float('inf')}

sol=-1
heap=[[0,0,0]]
dist[0][0]=0
while heap:
    
    cost, x,y = heappop(heap)
    
    if y==T:
        sol = cost
        break
    
    if dist[x][y] < cost:
        continue
    
    # 비둘기집, 최대 25 인덱스 이내의 암벽으로만 이동 가능
    for nx in range(x-2,x+3):
        for ny in range(y-2,y+3):
            if 0<=nx<=1000000 and 0<=ny<=T :
                if nx in G :
                    if ny in G[nx]:
                        if dist[nx][ny]>cost+1 :
                            dist[nx][ny]=cost+1
                            heappush(heap, [dist[nx][ny], nx,ny])        
print(sol)
