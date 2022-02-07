from collections import deque

N, P = map(int, input().split())

path=[[]for _ in range(N+1)]
capacity=[[0 for _ in range(N+1)] for _ in range(N+1)]
flow =[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(P):
    u, v = map(int, input().split())
    path[u].append(v)
    path[v].append(u)
    capacity[u][v]=1


sol=0
while True:
    prev = [-1 for _ in range(N+1)]
    q=deque([1])

    while (q):
        next = q.popleft()
        if next == 2:
            break

        for vertex in path[next]:
            if prev[vertex]==-1 and capacity[next][vertex] - flow[next][vertex]>0:
                q.append(vertex)
                prev[vertex]=next

    if prev[2]==-1:
        break

    
    vertex=2
    while True:
        if vertex==1:
            break
        flow[prev[vertex]][vertex]+=1
        flow[vertex][prev[vertex]]-=1
        vertex = prev[vertex]

    sol+=1

print(sol)