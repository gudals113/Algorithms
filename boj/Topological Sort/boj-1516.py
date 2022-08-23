# 게임 개발
# 위상정렬
# sol 220804 10:10-
from collections import deque

N = int(input())
inDegree = [0 for _ in range(N+1)]
toG = [ [] for _ in range(N+1) ]
time = [ 0 for _ in range(N+1)]
q= deque()
for s in range(1,N+1):
    l = list(map(int, input().split()))
    time[s] = l[0]
    inDegree[s] += len(l)-2    

    if inDegree[s]==0:
        q.append(s)
    
    for ei in range(1,len(l)-1):
        e=l[ei]
        toG[e].append(s)


saved = [ 0 for i in range(N+1)]
while q:
    s = q.popleft()
    
    saved[s]+=time[s]
    
    for next in toG[s]:
        inDegree[next]-=1
        saved[next] = max(saved[next], saved[s])
        
        if inDegree[next]==0:
            q.append(next)


for i in range(1,N+1):print(saved[i])