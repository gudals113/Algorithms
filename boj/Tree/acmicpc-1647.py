#도시 분할 계획, 최소 스패닝 트리, 크루스칼
import sys
input = sys.stdin.readline

def find(u):
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v)  : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return
    
    if abs(p[u]) >= abs(p[v]):
        p[u]+=p[v]
        p[v]=u
    
    else:
        p[v]+=p[u]
        p[u]=v
        
N, M = map(int, input().split())
p=[-1 for _ in range(N+1)]
path=[]
for _ in range(M): #u,v, cost
    path.append(list(map(int, input().split())))
path.sort(key= lambda x : x[2])

idx=0
sol=0
max_cost = 0
for i in range(M):
    u, v,cost = path[i]
    if find(u) == find(v):
        continue
    union(u,v)
    sol+=cost
    max_cost = max(max_cost,cost)
    idx+=1
    if idx == N:
        break

print(sol-max_cost)
    