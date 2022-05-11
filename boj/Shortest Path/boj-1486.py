#등산 dijikstra, 220510sol

from heapq import heappop, heappush

N,M,T,D = map(int,input().split())
G = [ [0 for _ in range(M)] for _ in range(N) ]
for i in range(N):
    line = input()
    for j in range(M):
        asc = ord(line[j])
        if asc >= 97 :
            G[i][j] = asc - 97 + 26
            
        else:
            G[i][j] = asc - 65

INF = float('inf')

def dij(i,j,k) : 
    dist = [ [ INF for _ in range(M)]  for _ in range(N)]
    dist[i][j]=k
    heap = []
    
    heappush(heap, [k,i,j])
    while heap:
        cost, x, y= heappop(heap)
        
        if dist[x][y] < cost:
            continue
        
        if dist[x][y] > D:
            continue
        
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<M :
                if abs(G[nx][ny] - G[x][y])>T:
                    continue
        
                elif G[nx][ny] > G[x][y] :
                    cost =(G[nx][ny]-G[x][y])**2
                    
                    if dist[nx][ny] > dist[x][y]+cost:
                        dist[nx][ny] = dist[x][y] + cost
                        heappush(heap, [dist[nx][ny],nx,ny])

                
                else :
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y]+1
                        heappush(heap, [dist[nx][ny],nx,ny])
    return dist

fromStart = dij(0,0,0)
answer = 0
for i in range(N):
    for j in range(M):
        if fromStart[i][j] <= D :
            fromMountain = dij(i,j,fromStart[i][j])
            if fromMountain[0][0] <= D:
                answer = max(answer,G[i][j])


print(answer)