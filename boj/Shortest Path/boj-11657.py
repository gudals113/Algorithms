#타임머신   (벨만포드)
N,M = map(int,input().split())
E = [ list(map(int,input().split())) for _ in range(M)]
INF = float('inf')
dist=[ INF for _ in range(N+1)]

def ford(s):
    dist[s]=0
    for i in range(N):
        for u,v,weight in E :
            if dist[v] > dist[u] + weight :
                dist[v] = dist[u]+weight
                
                if i==N-1:
                    return False
    return True

if ford(1):
    
    for i in range(2,N+1):
        if dist[i] == INF :
            print(-1)
        else:
            print(dist[i])
    
else:
    print(-1)