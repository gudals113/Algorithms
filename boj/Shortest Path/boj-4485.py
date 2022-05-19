# 녹색 옷 입은 애가 젤다지? (dijikstra) sol220513
from heapq import heappop, heappush
idx = 1
while True:
    N = int(input())
    if N== 0:
        break
    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))
    
    heap=[]
    dist = [ [float('inf') for _ in range(N)] for _ in range(N) ]
    heappush(heap,[G[0][0],0,0 ])
    dist[0][0] = G[0][0]
    while heap:
        cost, x, y = heappop(heap)
        
        
        if dist[x][y] > cost :
            continue
        
        
        for nx, ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<N :
                if dist[nx][ny] > cost + G[nx][ny] :
                    dist[nx][ny] = cost + G[nx][ny]
                    heappush(heap, [dist[nx][ny], nx,ny])
               
    print(f'Problem {idx}: {dist[N-1][N-1]}')
    idx+=1
    