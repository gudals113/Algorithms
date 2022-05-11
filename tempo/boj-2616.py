N,M,K = map(int, input().split())
G=[[] for _ in range(N+1)]
for _ in range(M):
    u,v,cost = map(int,input().split())
    G[u].append([v,cost]) 
    G[v].append([u,cost])
    
INF = float('inf')    
dist = [ [INF for _ in range(K+1)] for _ in range(N+1) ]
