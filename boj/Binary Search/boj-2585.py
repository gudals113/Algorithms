#2585번 경비행기
# 파라메트릭 서치
# sol 220913
from heapq import heappop, heappush
from math import ceil, sqrt


INF = float('inf')
N,K = map(int, input().split())
G = [[0,0]]
for _ in range(N):
    x,y = map(int, input().split())
    G.append([x,y])
G.append([10000,10000])

s = -1
e = 1500
def check(l):
    dist = [INF for _ in range(N+2)]
    heap = []
    dist[0]=0
    heappush(heap, [0, 0])
    while heap:
        cost, node = heappop(heap)

        if dist[node]<cost:
            continue
        

        if node == N+1 and cost<=K+1:
            return True

        if cost>=K+1:
            continue
        
        x,y = G[node] 
        for n in range(1, N+2):
            if dist[n] > cost + 1 :
                
                nx,ny = G[n]
                if ceil( sqrt((nx-x)**2 + (ny-y)**2) ) <= 10*l :
                    dist[n] = cost+1
                    heappush(heap, [dist[n], n])
                
    return False

#최대 연료통
answer =-1
while e-s>1:
    mid = (s+e)//2
    # print(mid)
    if check(mid):
        e = mid
        answer = mid
        
    else:
        s = mid

print(answer)