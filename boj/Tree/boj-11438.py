#LCA2
# DP로 풀이
# sol 220910 

import math, sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

N = int(input()) # 10만
tree = [ [] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

nodeDepth = [0 for _ in range(N+1)]
nodeParents = [[0 for _ in range(18)] for _ in range(N+1)]

visited=[0 for _ in range(N+1)]
def DFS(node, depth):        
    visited[node]=1
    
    for next in tree[node]:
        if not visited[next]:
            nodeParents[next][0] = node
            nodeDepth[next] = depth+1
            DFS(next,depth+1)
            
DFS(1,0)
for d in range(1,18):
    for node in range(1,N+1):
        parent = nodeParents[node][d-1]
        grandparent = nodeParents[parent][d-1]
        nodeParents[node][d] = grandparent
        
def lca(u,v):
    
    if nodeDepth[u] < nodeDepth[v]:
        u, v = v, u

    # depthU -> depthV
    if nodeDepth[u] > nodeDepth[v]:
        
        for i in range(17,-1,-1):
            if nodeDepth[u] - nodeDepth[v] >= 2**i:
                u = nodeParents[u][i]
    
    if u==v:
        return u
    
    for i in range(17,-1,-1):
        if nodeParents[u][i] != nodeParents[v][i]:
            u= nodeParents[u][i]
            v = nodeParents[v][i]
    
    return nodeParents[u][0]

M = int(input()) # 10만
for _ in range(M):
    u,v = map(int, input().split())
    rst  = lca(u,v)
    print(rst)