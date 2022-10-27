# LCA
# sol 220910 
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def lca(u,v):
    depthU , depthV = nodeInfo[u][1], nodeInfo[v][1]

    
    if depthU > depthV:
        while depthU > depthV:
            u = nodeInfo[u][0]
            depthU-=1

        
    elif depthU < depthV:
        while depthV > depthU:
            v = nodeInfo[v][0]
            depthV-=1
    
    while u!=v:
        u, depthU = nodeInfo[u][0], depthU-1
        v, depthV = nodeInfo[v][0], depthV-1
    
    return u
    
N = int(input()) # 5만
tree = [ [] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

nodeInfo = [ [-1,-1] for _ in range(N+1)]
nodeInfo[1] = [-1, 0]
# 노드의 부모와 깊이 저장
visited=[0 for _ in range(N+1)]
def DFS(node, depth):
    
    visited[node]=1
    
    for next in tree[node]:
        if not visited[next]:
            nodeInfo[next] = [node, depth+1]
            DFS(next,depth+1)
DFS(1,0)

M = int(input())
for _ in range(M):
    u,v = map(int, input().split())
    rst  = lca(u,v)
    print(rst)