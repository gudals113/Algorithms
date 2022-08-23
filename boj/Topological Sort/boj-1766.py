# boj-1766.py
# 문제집
# topologi
# sol 220729
from heapq import heappop, heappush


N,M = map(int, input().split())
toG = [ [] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    
    toG[s].append(e)
    inDegree[e]+=1
    
heap = []
for i in range(1,N+1):
    if inDegree[i]==0:
        heappush(heap, i)
        
answer = []
while heap:
    solved = heappop(heap)
    answer.append(solved)
    for next in toG[solved]:
        inDegree[next]-=1
        if inDegree[next]==0:
            heappush(heap, next)
        
print(*answer)