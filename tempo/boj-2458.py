#키 순서 # 플로이드 와샬 / DFS
# import sys
# input = sys.stdin.readline
# N,M =map(int,input().split())
# INF = float('inf')
# dist = [ [INF for _ in range(N+1)]for _ in range(N+1)]
# for _ in range(M):
#     u,v = map(int,input().split())
#     dist[u][v] = 1
    
# for i in range(1,N+1):
#     dist[i][i]=0

# for k in range(1,N+1):
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]

# sol = N
# for i in range(1,N+1):
#     for j in range(1,N+1):
#         if dist[i][j]==INF and dist[j][i]== INF:    
#             sol-=1
#             break
# print(sol)

import sys
input = sys.stdin.readline
N,M =map(int,input().split())
toG = [ []for _ in range(N+1)]
fromG=[ []for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    toG[u].append(v)    #내가 향하는 노드
    fromG[v].append(u)  #나를 향하고 있는 노드


    
def toDFS(node):
    visited[node]=1
    for next in toG[node]:
        if not visited[next]:
            toDFS(next)

    return

def fromDFS(node):
    visited[node]=1
    for next in fromG[node]:
        if not visited[next]:
            fromDFS(next)
    return 

sol=0
for i in range(1,N+1):
    visited=[0 for _ in range(N+1)]
    toDFS(i)
    fromDFS(i)
    tmp=0
    for i in range(1,N+1):
        if visited[i]:
            tmp+=1
    if tmp==N:
        sol+=1
        
print(sol)