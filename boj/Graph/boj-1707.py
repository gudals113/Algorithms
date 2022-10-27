# 이분 그래프
# 220830 sol
# BFS
from collections import deque
import sys
input = sys.stdin.readline

def BFS(G):
    visited = [0 for _ in range(V+1)]
    for i in range(1,V+1):
        if visited[i]==0:
            q = deque([i])
            visited[i]=1
            while q:  
                node = q.popleft()
                
                nodeTeam = visited[node]
                nextTeam = nodeTeam*-1
                for next in G[node]:
                    if visited[next]==0:
                        visited[next] = nextTeam
                        q.append(next)
                                
                    elif visited[next] == nodeTeam:
                        return 'NO'
    return 'YES'

T = int(input())
for _ in range(T):
    answer='YES'
    
    V,E = map(int,input().split())
    # graph = [[0 for _ in range(V+1)] for _ in range(V+1)]
    G = [ [] for _ in range(V+1)]

    for i in range(E):
        u,v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
        
    answer = BFS(G)
    print(answer)