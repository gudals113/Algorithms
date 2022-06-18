#줄세우기 위상정렬 sol 220601 
from collections import deque


N, M = map(int, input().split())
G = [ [] for _ in range(N+1)]
inG = [ 0 for _ in range(N+1)]

for _ in range(M) :
    A, B = map(int, input().split())
    G[A].append(B) 
    inG[B]+=1
    
q=deque()
for i in range(1,N+1):
    if inG[i]==0:
        q.append(i)
        
        
            
answer = []
while q:
    now = q.popleft()
    answer.append(now)
    
    for next in G[now]:
        inG[next]-=1
        if inG[next]==0:
            q.append(next)

print(*answer)
    