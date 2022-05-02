#친구비 (union find / BFS)
from collections import deque
N, M, k = map(int, input().split())
A = [0]+list(map(int, input().split()))
friend=[ [] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
    
p = [-1 for _ in range(N+1)]
def find(u):
    if p[u]<0:
        return u

    p[u]=find(p[u])
    return p[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v:
        return
    if A[u] >= A[v]:    #친구비가 적은 사람을 루트 노드로 유니온
        p[u] = v
    else:
        p[v] = u

for i in range(1,N+1):
    for n in friend[i]:
        union(i,n)

need=0
for i in range(1,N+1):
    if p[i]==-1:
        need+=A[i]
        
if need <= k :
    print(need)
else:
    print('Oh no')


#########################BFS#########################BFS#########################BFS
# from collections import deque
# N, M, k = map(int, input().split())
# A = [0]+list(map(int, input().split()))
# friend=[ [] for _ in range(N+1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     friend[a].append(b)
#     friend[b].append(a)

# visited = [-1 for _ in range(N+1)]

# def BFS(idx):
#     money = A[idx]
#     q=deque([idx])
#     while q:
#         node = q.popleft()
#         for f in friend[node] :
#             if visited[f] ==-1:
#                 visited[f] =1
#                 q.append(f)
#                 if A[f] < money:   #친구비 적은 사람으로 갱신 후 리턴
#                     money = A[f]
#     return money

# need=0
# for i in range(1,N+1):
#     if visited[i]==-1:
#         visited[i]=1
#         need += BFS(i)
        
# if need <= k :
#     print(need)
# else:
#     print('Oh no')

