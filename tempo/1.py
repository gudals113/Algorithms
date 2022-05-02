from heapq import heappop, heappush

N,M,K,X= map(int, input().split())
G=[ []for _  in range(N+1) ]
for _ in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    
INF = float('inf')
heap =[]    
dist= [INF for _ in range(N+1)]
dist[X]=0
visited=[0 for _ in range(N+1)]

heappush(heap, [0,X])

while heap:
    cost, node = heappop(heap)
    if not visited[node]:
        visited[node]=1
        for next in G[node]:
            if not visited[next] :
                if dist[next] > dist[node]+1:
                    dist[next]=dist[node]+1
                    heappush(heap,[ dist[next], next]) 


sol = []
for i in range(1,N+1):
    if dist[i]==K:
        sol.append(i)
if len(sol)==0:
    print(-1)
else:
    for x in sol:
        print(x)