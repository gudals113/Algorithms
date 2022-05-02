#열혈강호 3
from collections import deque

N,M = map(int, input().split())

path = [ [] for _ in range(N+M+2) ]
capacity= [ [0 for _ in range(N+M+2)] for _ in range(N+M+2)]
flow= [ [0 for _ in range(N+M+2)] for _ in range(N+M+2)]

for i in range(1,N+1):
    capacity[0][i] = 1
    
    path[0].append(i)
    path[i].append(0)
    
for i in range(N+1, N+M+1):
    path[i].append(N+M+1)
    path[N+M+1].append(i)

for i in range(N):
    l = list(map(int,input().split()))
    for j in range(1, l[0]+1):
        path[i].append( l[j]+N )
        path[l[j]+N].append(i)
         
        capacity[i][ l[j]+N ] +=1
        capacity[l[j]+N][N+M+1] =1

sol=0
while True:
    prev = [-1 for _ in range(N+M+2)]
    q=deque([0])
    
    while q:
        node = q.popleft()
        
        for next in path[node]:
            if prev[next]==-1 and capacity[node][next] - flow[node][next] > 0 :
                prev[next]=node
                q.append(next)
    
    if prev[N+M+1] == -1:
        break 
    
    node = N+M+1
    while node !=0:
        before = prev[node]
        
        flow[before][node] +=1
        flow[node][before] -=1
        
        node = before
    
    sol +=1

print(sol)