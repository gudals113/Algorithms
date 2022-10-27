from collections import deque
from heapq import heappop, heappush
N = 1
G = []
#모든 간선 정보 저장
E = []

#1. 다익스트라 O(E log E) = O(E log V)
def deijkstar(start):
    dist = [float('inf') for _ in range(N)]
    dist[start]=0
    heap = [[0,start]]
    
    while heap:
        cost, node = heappop(heap)
        if dist[node] < cost:
            continue
        for next,weight in G[node]:
            if dist[next]> weight+cost:
                dist[next] = weight+cost
                heappush(heap, [dist[next], next])
    # return dist[dest]

#2. 음수 가중치,하나의 정점에서 모든 정점으로 가는 최단 거리
# 벨만 포드 O(VE)

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

def bellman(start):
    dist = [float('inf') for _ in range(N)]
    dist[start] = 0
    
    for i in range(N):
        for u,v,weight in E :
            if dist[v] > dist[u] + weight :
                dist[v] = dist[u]+ weight
                if i==N-1:
                    if canEnd(v):
                        return False
                
    return True

#3. 모든 정점에서 모든 정점으로 가는 최단거리
# 플로이드 워셜 O(V^3)
def floyd():
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


                
                
                