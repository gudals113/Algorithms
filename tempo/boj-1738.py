from collections import deque
N,M = map(int, input().split())
E=[]
G=[[]for _ in range(N+1)]
for _ in range(M):
    u,v,w = map(int,input().split())
    w= w*-1
    E.append([u,v,w])
    G[u].append(v)
INF = float('inf')

#BFS
def canEnd(start):
    q= deque([start])
    visited = [0 for _ in range(N+1)]
    visited[start]=1
    while q:
        node = q.popleft()
        if node == N :
            return True
        for next in G[node]:
            if not visited[next] :
                visited[next]=1
                q.append(next)
    
    return False
    
#Bellman Ford
def BF():
    dist = [[INF,0] for _ in range(N+1)]
    dist[1][0]=0
    
    for i in range(N):
        for u,v,cost in E:
            if dist[v][0] > dist[u][0]+cost :
                dist[v][0] = dist[u][0]+cost
                dist[v][1] = u
                
                if i == N-1:
                    if canEnd(u):
                        return [-1]  
                    else:
                        continue
               
    node = N
    sol = []
    while True:
        sol.append(node)
        if node == 1:
            break
        node = dist[node][1]
    return sol[::-1]

rst = BF()
print(*rst)

## 새로운 풀이
# import sys
# import math
# input = lambda:sys.stdin.readline().strip()
# n,m = map(int,input().split())
# inf = math.inf
# graph = [[] for _ in range(n+1)]
# distance = [-inf for _ in range(n+1)]
# router = [-1 for _ in range(n+1)]
# for _ in range(m):
#     u,v,w = map(int,input().split())
#     graph[u].append((v,w))
# distance[1] = 0
# for iter in range(n):
#     for current in range(1,n+1):
#         for next, cost in graph[current]:
#             if distance[current] != -inf and distance[current] + cost > distance[next]:
#                 distance[next] = distance[current] + cost
#                 router[next] = current
#                 if iter == n- 1:
#                     distance[next] = inf
# res = [n]
# if distance[n] != inf:
#     current = n
#     while current != 1:
#         current = router[current]
#         res.append(current)
#     res.reverse()
#     print(*res)
# else:
#     print(-1)



## 새로운 시도 (틀림)
## 2N 번 돌리고 체크 이용해서 벨만 포드는 안되나?
# from collections import deque

# N,M = map(int, input().split())
# E=[]
# G=[[]for _ in range(N+1)]
# for _ in range(M):
#     u,v,w = map(int,input().split())
#     w= w*-1
#     E.append([u,v,w])
#     G[u].append(v)
# INF = float('inf')

# #BFS
# def canEnd(start):
#     q= deque([start])
#     visited = [0 for _ in range(N+1)]
#     visited[start]=1
#     while q:
#         node = q.popleft()
#         if node == N :
#             return True
#         for next in G[node]:
#             if not visited[next] :
#                 visited[next]=1
#                 q.append(next)
    
#     return False
    
# #Bellman Ford
# def BF():
#     dist = [[INF,0] for _ in range(N+1)]
#     dist[1][0]=0
#     for i in range(3*N):
#         for u,v,cost in E:
#             if dist[v][0] > dist[u][0]+cost :
#                 dist[v][0] = dist[u][0]+cost
#                 dist[v][1] = u
                
#         if i == N-2:
#             check = dist[N][0]  
            
#             node = N
#             sol = []
#             while True:
#                 sol.append(node)
#                 if node == 1:
#                     break
#                 node = dist[node][1]
                 
                         
#         elif i == 3*N-1:
#             if check != dist[N][0]:
#                 return [-1]
        
#     return sol[::-1]

# rst = BF()
# print(*rst)

