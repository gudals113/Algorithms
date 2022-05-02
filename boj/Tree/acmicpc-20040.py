#사이클 게임 union find
import sys
sys.setrecursionlimit(10**5)
def find(u):
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v:
        return True
    
    if abs(p[u]) >= abs(p[v]):
        p[u]+=p[v]
        p[v]=u
    else:
        p[v]+=p[u]
        p[u]=v
    return False

N, M = map(int, input().split())
p=[-1 for _ in range(N)]      
sol=0
for i in range(M):
    a,b = map(int, input().split())
    if union(a,b) == True:
        sol = i+1
        break
print(sol)