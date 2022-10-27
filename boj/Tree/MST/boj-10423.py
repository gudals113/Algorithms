# 전기가 부족해
# MST

# from heapq import heappop, heappush

# def find(u):
    
#     if p[u]<0 or u in devDict:
#         return u
    
#     p[u] = find(p[u])
#     return p[u]

# def union(u,v):
#     u,v = find(u), find(v)
#     if u==v : return False
#     if p[u]>0 and p[v]>0: return False
    
#     if p[u] < 0 :
#         p[u]=v
#     else:
#         p[v]=u
#     return True


# N,M,K = map(int, input().split())
# DEV = list(map(int, input().split()))
# G = [[]for _ in range(N+1)]
# heap=[]
# for _ in range(M):
#     u,v,w = map(int, input().split())
#     G[u].append([v,w])
#     G[v].append([u,w])

#     heappush(heap,[ w, u, v])

# p = [-1 for _ in range(N+1)]
# devDict ={}
# for city in DEV:
#     p[city] = city
#     devDict[city]=1

# answer = 0
# while heap:
#     w,u,v = heappop(heap)
    
#     if union(u,v): answer+=w
    
# print(answer)
    
# boj-10423.py

from heapq import heappop, heappush

def find(u):
    
    if p[u]<0 :
        return u
    
    p[u] = find(p[u])
    return p[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v: return False
    
    if p[v] < 0 :
        p[v]=u
    else:
        p[u]=v
    return True


N,M,K = map(int, input().split())
DEV = list(map(int, input().split()))
G = [[]for _ in range(N+1)]
heap=[]
for _ in range(M):
    u,v,w = map(int, input().split())
    G[u].append([v,w])
    G[v].append([u,w])

    heappush(heap,[ w, u, v])

p = [-1 for _ in range(N+1)]

for i in range(1, K):
    u,v = DEV[i-1], DEV[i]
    union(u,v)

answer = 0
while heap:
    w,u,v = heappop(heap)
    
    if union(u,v): answer+=w
    
print(answer)
    
