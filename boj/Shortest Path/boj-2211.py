#네트워크 복구, 다익스트라, sol 220611
#직전 노드 저장하고 answer배열에 중복 확인하며 추가 할 필요 없이 바로 추가해도 문제 없다.

from heapq import heappop, heappush


N,M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v,cost = map(int,input().split())
    G[u].append([v,cost])
    G[v].append([u,cost])
INF = float('inf')
init = [[INF,i] for i in range(N+1)]

init[1]=[0,0]

heap = []
heappush(heap, [0,1])
while heap:
    cost, node = heappop(heap)
    if cost > init[node][0]:
        continue
    
    for next,weight in G[node]:
        if init[next][0] > cost+weight:
            init[next][0]=cost+weight
            init[next][1]=node
            heappush(heap, [ init[next][0], next ])
       
answer = [ [] for _ in range(N+1)]
sol=0
for u in range(2, N+1):
    v = init[u][1]
    
    if u > v : 
        if u not in answer[v]:
            sol+=1
            answer[v].append(u)
        
    else : 
        if v not in answer[u]:
            sol+=1
            answer[u].append(v)
            
print(sol)     
for u in range(1,N+1):
    for v in answer[u]:
        print(u, v)