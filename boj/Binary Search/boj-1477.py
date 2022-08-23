# 휴게소 세우기
# sol 220809
# 이분 탐색, 매개 변수 탐색

from collections import deque
from heapq import heappop, heappush

N, M, L = map(int, input().split())
G = list(map(int, input().split()))
G.append(0)
G.append(L)
G.sort()

D=[]
s,e=-1,-1
for i in range(1,N+2):
    dist = G[i]-G[i-1]
    D.append(dist)
    e = max(dist+1, e)
D.sort(reverse=True)

def check(maxLength):
    count = 0
    tmp = deque()
    # rest = -(maxLength-1)
    for dist in D:
        if dist>maxLength:
            count+=1
            tmp.append(dist-maxLength)
        else:
            break
    
    while tmp :
        dist = tmp.popleft()
        if dist>maxLength:
            count+=1
            tmp.append(dist-maxLength)

        if count>M :
            return count
        
    return count

answer = 0
while e-s>1:
    mid = (e+s)//2
    count = check(mid)
    if count <= M :
        e = mid
        answer = mid
    
    else : 
        s = mid
        
print(answer)