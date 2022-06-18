#나만 안되는 연애, MST, sol 220611
from heapq import heappop, heappush

N,M = map(int,input().split())
collage = ['']+list(input().split())

heap=[]
p = [ -1 for _ in range(N+1)]
for _ in range(M):
    u,v,d = map(int,input().split())
    heappush(heap, [d,u,v])

def find(u):
    if p[u]<0 : 
        return u
    
    p[u]=find(p[u])
    return p[u]

def union(u,v):
    u = find(u)
    v = find(v)
    
    if u==v:
        return False
    
    p[u]=v
    return True

answer = 0
while heap:
    cost,u,v = heappop(heap)
    if collage[u]!=collage[v]:
        if union(u,v):
            answer+=cost
           
count=0 
for i in range(1,N+1):
    if p[i]<0 :
        count+=1
        
    if count>1:
        answer=-1
        break
    
print(answer)
            