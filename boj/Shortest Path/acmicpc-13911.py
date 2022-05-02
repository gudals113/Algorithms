from heapq import heappop, heappush

INF = float('inf')
V,E = map(int, input().split())
G=[ [] for _ in range(V+3)]

for _ in range(E):
    u,v,w = map(int, input().split())
    G[u].append([v,w])
    G[v].append([u,w])
    
M,x = map(int,input().split())
mac = list( map(int, input().split()) )
S,y = map(int, input().split())
star = list( map(int, input().split()) )

virtualM = V+1
virtualS = V+2

for m in mac:
    G[m].append([virtualM, 0])
    G[virtualM].append([m,0])

for s in star:
    G[s].append([virtualS,0] )
    G[virtualS].append([s,0])


def dij(start):
    dist=[INF for _ in range(V+3)]
    visited=[ 0 for _ in range(V+3)]
    heap=[]
    dist[start]=0
    heappush(heap, [0, start])
    
    while heap:
        cost, node = heappop(heap)
        if visited[node]==0:    
            visited[node]=1
            
            for next, w in G[node]:
                if next == virtualM or next == virtualS :
                    continue
                if visited[next] == 0:
                    if dist[next] > w + cost:
                        dist[next] = w + cost
                        heappush(heap, [ dist[next], next])
    return dist
                   
distMtoH = dij(virtualM)
distStoH = dij(virtualS)

sol=INF
for i in range(1, V+1):
    if i in mac or i in star:           #    시발 여기서 1시간 날렸다.
        continue
    if distMtoH[i] <=x and distStoH[i]<=y :
        sol = min(sol, distMtoH[i] + distStoH[i] )
        
if sol==INF:
    print(-1)
else:
    print(sol)
