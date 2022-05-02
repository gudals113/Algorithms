from collections import deque


N= int(input())
tree=[ [ ]for _ in range(N+1) ]
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

ans=[ 0 for _ in range(N+1) ]
visited=[ 0 for _ in range(N+1)]
q=deque([1])
visited[1]=1
while q:
    parent = q.popleft()
    
    for child in tree[parent]:
        if visited[child]==0:
            visited[child]=1
            ans[child]=parent
            q.append(child)

for i in range(2, N+1):
    print(ans[i])