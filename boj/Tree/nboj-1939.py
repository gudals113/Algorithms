#중량 제한 (union-find / binary search+bfs)
#-c로 입력 받아서 돌리면 되는데 못 떠올림
# 시간 초과 코드
from collections import deque
N,M = map(int,input().split())
path = [ []for _ in range(N+1) ]
p=[-1 for _ in range(N+1)]
for _ in range(M):
    A,B,C = map(int,input().split())
    path[A].append([B,C])
    path[B].append([A,C])
start, end = map(int,input().split())

visited=[-1 for _ in range(N+1)]
q=deque([[start,0]]) # 노드, 노드에 오는 동안 버틸 수 있는 가장 큰 무게 ( 경로에 있는 최소 무게들 중에서 최대 )
visited[start] = float('inf')
while q:
    node, maxCost = q.popleft()
    for next, d in path[node]:
        if visited[next] ==-1 :
            visited[next] = min(visited[node], d)
            q.append([next, visited[next]])
        else:
            if visited[next] < d and visited[next] < visited[node] :
                visited[next] = min(visited[node], d)
                q.append([next, visited[next]])
                
print(visited[end])