# boj-1368.py
from heapq import heappop, heappush

def find(u):
    if p[u]<0:
        return u
    
    p[u]  = find(p[u])
    return p[u]
def union(u,v):
    u = find(u)
    v = find(v)
    if u==v:
        return
    
    p[u]=v
    return
    
N = int(input())
heap = []
for i in range(N):
    dig = int(input())
    heappush(heap, [dig,i, i+N])
    
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(i+1,N):
            heappush(heap, [l[j], i+N,j+N ])
            
p=[-1 for _ in range(2*N)]
for i in range(1,N):
    p[i]=0

answer = 0
count=0 
while heap:
    if count == N:
        break
    cost, u, v = heappop(heap)
    
    if find(u)!=find(v):
        union(u,v)
        answer+=cost
        count+=1
    
    
print(answer)