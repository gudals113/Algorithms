from collections import defaultdict


N = int(input())
d = defaultdict(int)
L = []
tmp = []
for _ in range(N):
    h,o = map(int, input().split())
    if h>o:
        h,o = o,h
        
    tmp.append([h,o])


D = int(input())
for i in range(N):
    h,o = tmp[i]
    if o-h>D:
        continue
    
    start = o-D
    end = h+1
    d[start]+=1
    d[end]-=1
    L.append(start)
    L.append(end)
    
    
L = list(set(L))
L.sort()
prefix=[0]

for i in range(len(L)):
    #좌표.
    p = L[i]

    prefix.append(prefix[-1]+d[p])

print(max(prefix))