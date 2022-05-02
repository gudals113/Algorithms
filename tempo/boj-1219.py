#오민식의 고민
from collections import deque
INF = float('inf')
N,start,end,M = map(int,input().split())
E = []

G=[[] for _ in range(N) ]

for _ in range(M):
    u,v, weight = map(int,input().split())
    E.append([u,v,weight])
    
    G[u].append(v)
    
earning = list((map(int, input().split())))
dist = [INF for _ in range(N)]
def ford(start):
    dist[start]=-earning[start]
    
    for i in range(N):
        for u,v,cost in E:
            if dist[v] > dist[u]+cost-earning[v]:
                dist[v] = dist[u]+cost-earning[v]

                
                if i == N-1:
                    if canEnd(u):
                        return False
                    else:
                        continue
    
    return True


def canEnd(s):
    visited=[0 for _ in range(N)]
    q=deque([s])
    while q:
        node = q.popleft()
        if node == end:
            return True
        if visited[node] :
            continue
        visited[node]=1
        for next in G[node]:
            if visited[next]==0:
                q.append(next)
    return False

result = ford(start)

if dist[end]==INF:
    print('gg')
else:
    if result:
        print(dist[end]*-1)
    else:
        print('Gee')


#다른 풀이 : https://lookbackonlife.tistory.com/22