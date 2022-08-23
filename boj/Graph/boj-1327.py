# 소트 게임 
# Bfs
# try 220706 - > hint 220707
from collections import deque

N, K = map(int, input().split())
L = list( input().split()) 
visited = set("".join(L))

q=deque()
q.append([0,L])

check = sorted(L)
ans = -1

while q:
    t, l = q.popleft()
    # print(l)
    if l == check:
        ans = t
        break
    

    for i in range(N-K+1):
        newl = l[:]
        target = l[i:i+K]
        target=target[::-1]
        
        for j in range(K):
            newl[i+j]=target[j]

        # print(newl)
        neww = "".join(newl)
        
        if neww not in visited:
            visited.add(neww)
            q.append([t+1, newl])

print(ans)