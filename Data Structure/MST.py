#1. 크루스탈 O(E log E)
def find(u) :
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return False
    
    if u < v:
        p[v]=u
    else:
        p[u]=v
    return True

E = 1
V = 1
p=[-1 for _ in range(V+1)]
G=[]
# G 정렬 해주어야 한다.
sol=0
idx=0
for i in range(E):
    u,v,cost = G[i]
    if union(u,v):
        sol+=cost
        idx+=1
    
    if idx == V-1:
        break
    
    
# 2. 프림 알고리즘 O(E log V)
import heapq
V,E = map(int,input().split())
G = []
heap  =[[0, 1]] #가중치, 노드
sol= 0
visited=[0 for _ in range(V+1)]
count=0

while count<V:
    cost, node = heapq.heappop(heap)
    if not visited[node]:
        visited[node]=1
        sol+=cost
        count+=1
        
        for next,cost in G[node]:
            if not visited[next] :
                heapq.heappush(heap, [cost,next ])
