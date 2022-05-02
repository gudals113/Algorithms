#별자리 만들기 (MST)
from heapq import heappop, heappush
import math
N = int(input())
star = []
for i in range(N):
    star.append(list(map(float, input().split())))

G = [ [0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    x,y = star[i]    
    
    for j in range(i, N):
        nx,ny = star[j]
    
        dist = math.sqrt((x-nx)**2 + (y-ny)**2)
        G[i][j]= dist
        G[j][i]= dist

heap=[]
heappush(heap, [0, 0])
sol=0
visited=[0 for _ in range(N)]

while heap:
    cost, node = heappop(heap)
    if visited[node]==1:
        continue
    
    sol+=cost
    visited[node]=1
    
    x,y = star[node]
    for next in range(N):
        if visited[next]==0 :
            nx,ny = star[next]
            dist = math.sqrt((x-nx)**2 + (y-ny)**2)
            heappush(heap, [dist,next])
            
print(f'{sol:.2f}')
    