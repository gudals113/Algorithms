#A->B, BFS, sol 220609
from collections import deque

S,R = map(int,input().split())

q = deque()
q.append([1,S])
ans = -1
while q:
    sol, num = q.popleft()
    if num == R:
        ans = sol
        break
    
    tmp1, tmp2 = num*2, int(str(num)+'1')
    if tmp1<=R:
        q.append([sol+1, tmp1])
        
    if tmp2<=R:
        q.append([sol+1, tmp2])
        
print(ans)
