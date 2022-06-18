#거짓말 union-find sol220524
def find(u):
    if p[u] < 0:
        return 
    
    p[u] = find(p[u])
    return p[u]

def union(u,v):
    u=find(u)
    v=find(v)
    if u == v:
        return
    
    if u==0 :
        p[u] -= abs(p[v])
        p[v]=u
    else :
        p[v] -= abs(p[u])
        p[u]=v
    

N,M = map(int,input().split())
T = list(map(int, input().split()))
L = []
for _ in range(M):
    
    line = list(map(int, input().split()))
    L.append(line)
    
p = [-1 for _ in range(N+1)]

if T[0]>=1:
    for i in range(1, 1+T[0]):
        union(0,T[i])

for i in range(M):
    line = L[i]
    if line[0] >=2 :
        for i in range(2, 1+line[0]):
            union(line[i-1],line[i])

compare = 0    
truth = 0
for i in range(M):
    target = L[i][1]
    if find(target) == compare :
        truth+=1
print(M-truth)