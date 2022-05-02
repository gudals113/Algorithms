#네트워크 연결, 최소 스패닝 트리, 크루스칼
def find(u) -> int:
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) -> None : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return
    
    if u < v:
        p[v]=u
    else:
        p[u]=v

N, M = int(input()), int(input())
p=[-1 for _ in range(N+1)]
network=[]
for _ in range(M):
    info = list(map(int, input().split()))
    network.append(info)
network.sort(key= lambda x : x[2])

idx=0
sol=0
for i in range(M):
    u, v,cost = network[i]
    if find(u) == find(v):
        continue
    union(u,v)
    sol+=cost
    idx+=1
    if idx == N:
        break
print(sol)