#최소 스패닝 트리 왜  

#크루스칼 알고리즘 (e log e)
# def find(u) :
#     if p[u]<0:
#         return u
#     p[u] = find(p[u])
#     return p[u]

# def union(u,v) : #v가 루트가 된다.
#     u,v = find(u),find(v)
#     if u==v:
#         return
    
#     if u < v:
#         p[v]=u
#     else:
#         p[u]=v

# V,E = map(int,input().split())
# p=[-1 for _ in range(V+1)]
# graph=[]
# for _ in range(E):
#     A, B ,C = map(int,input().split())
#     graph.append([A,B,C])
# graph.sort(key=lambda x:x[2])
    
# sol=0
# idx=0
# for i in range(E):
#     x,y,cost = graph[i]
#     if find(x)!=find(y):
#         union(x,y)
#         sol+=cost
#         idx+=1
    
#     if idx == V-1:
#         break
    
# print(sol)

#프림 알고리즘 O(e log v)

import heapq
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
graph = [ [] for _ in range(V+1)]

for _ in range(E):
    A, B ,C = map(int,input().split())
    graph[A].append([B,C]) 
    graph[B].append([A,C])


heap=[]
sol= 0
visited=[0 for _ in range(V+1)]
heapq.heappush(heap, [0, 1]) #가중치, 노드
count=0

while count<V:
    cost, node = heapq.heappop(heap)
    if not visited[node]:
        
        visited[node]=1
        sol+=cost
        count+=1
        
        for v,c in graph[node]:
            if not visited[v] :
                heapq.heappush(heap, [ c, v ])
print(sol)



