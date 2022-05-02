#우주신과의 교감 프림 알고리즘
import heapq
import math
N, M = map(int,input().split())

space=[[-1,-1] ]

for i in range(1,N+1):
    x,y = map(int,input().split())
    space.append([x,y])
    
placed=[[0 for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    x,y = map(int, input().split())
    placed[x][y]=1
    placed[y][x]=1
    
       
q = []
visited=[-1 for _ in range(N+1)]

sol=0.00
count=0#이미 연결된 노드 수

heapq.heappush(q, [0.00,1]) #가중치, 노드
while count<N:
    dist, node = heapq.heappop(q)    
    if visited[node] ==1:
        continue
    
    visited[node]=1
    sol+=dist
    count+=1

    for i in range(1,N+1):
        if visited[i]!=1:
            
            if placed[node][i] ==1 :        #이미 연결된 경로의 경우 거리 0으로 heap push
                heapq.heappush(q, [0.00,i])
                
            elif node!=i :
                
                dist_node_i = math.sqrt( (space[node][0] - space[i][0] )**2 + ( space[node][1] - space[i][1] )**2 )
                heapq.heappush(q, [dist_node_i,i])
    
print(f'{sol:.2f}')