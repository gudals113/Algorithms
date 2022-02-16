#트릐의 부모 찾기 BFS
from collections import deque


N=int(input())
sol = [0 for _ in range(N+1)]
tree = [[]for _ in range(N+1)]

for i in range(N-1):
    nodeA, nodeB = map(int, input().split())
    
    tree[nodeA].append(nodeB)
    tree[nodeB].append(nodeA)

visited = [ 0 for _ in range(N+1)]
q=deque([1])
visited[1]=1
while q:
    now = q.popleft()
    children = tree[now]
    for child in children:
        if visited[child] == 0:
            sol[child] = now
            visited[child] =1
            q.append(child)
for i in range(2,N+1):
    print(sol[i])

    