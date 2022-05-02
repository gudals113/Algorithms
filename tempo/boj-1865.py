T= int(input())
INF = float('inf')
def BF(start):
    dist[start]=0
    for i in range(N):
        for u in range(1,N+1):
            for v in range(1,N+1):
                
                if dist[v] > dist[u]+G[u][v]:
                    dist[v]=dist[u]+G[u][v]
            
                    if i == N-1 :
                        return True
    return False
            

for _ in range(T):
    N,M,W = map(int,input().split())
    G = [ [10001 for _ in range(N+1)] for _ in range(N+1) ]
    for _ in range(M):
        S,E,T = map(int,input().split())
        G[S][E]= min(G[S][E], T)
        G[E][S]= G[S][E]
        
    for _ in range(W):
        S,E,T = map(int,input().split())
        G[S][E]= min(G[S][E], -T)
        
    dist = [INF for _ in range(N+1)]
    rst = BF(1) 
    if rst : 
        # print(dist)
        print('YES')
        
    else:
        print('NO')