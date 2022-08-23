# coolest ski route
# sol 220805
# 위상 정렬
# 벨만 포드로도 깔끔하게 풀 수 있다.


N, M = map(int, input().split())
INF = float('inf')

E=[]
for _ in range(M):
    u,v,c = map(int, input().split())
    E.append([u,v,-1*c])
    
for i in range(1,N+1):
    E.append([0,i,0])

def ford(s):
    dist = [ INF for _ in range(N+1)]
    dist[s] = 0
    for i in range(N+1):
        for u,v,w in E:
            if dist[v] > dist[u] + w : 
                dist[v] = dist[u] + w
                
                if i==N :
                    return INF
    return min(dist)



rst = ford(0)
print(rst*-1)
#
# saved = [0 for _ in range(N+1)]
# q= deque()
# for i in range(1,N+1):
#     if inDegree[i]==0:
#         q.append(i)

# while q:
#     node = q.popleft()
#     for next, weight in G[node]:
#         inDegree[next]-=1
#         saved[next] = max(saved[next], saved[node]+weight)
        
#         if inDegree[next]==0:
#             q.append(next)

# print(max(saved))
    