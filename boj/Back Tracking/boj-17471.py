# # boj-17471.py
# # 게리맨더링
# # 220805 11:40-
# # 13:32 hint 알고리즘 분류

# # 도저히 유니온 파인드로는 안될 것 같고 N=10이니까 어쩔 수 없이 완전 탐색해야 될 것 같았는데 잘 안돼서 알고리즘 분류 확인함

from collections import deque
from itertools import combinations
INF = float('inf')
N = int(input())
ppl = [0]+list(map(int, input().split()))
SUMPPL = sum(ppl)

G = [[]for _ in range(N+1)]
for i in range(1,N+1):
    l = list(map(int, input().split()))
    
    for next in (l[1:]):
        G[i].append(next)

answer = INF

def check(l1,l2): 
    global answer
    q1 = deque([l1[0]])
    q2 = deque([l2[0]])
    sum1 = ppl[l1[0]]
    sum2 = ppl[l2[0]]

    visited=[0 for _ in range(N+1)]
    visited[l1[0]]=1
    visited[l2[0]]=1
    
    while q1 :
        city = q1.popleft()
        for next in G[city]:
            if next in l1 and not visited[next]:
                visited[next]=1
                sum1+=ppl[next]
                q1.append(next)
                
    while q2 :
        city = q2.popleft()
        for next in G[city]:
            if next in l2 and not visited[next]:
                visited[next]=1
                sum2+=ppl[next]
                q2.append(next)
                
    if visited.count(0) == 1:
        answer = min(answer, abs(sum1-sum2))


def DFS(idx,l1):
    if len(l1) == N//2 +1 :
        return

    l2 = []
    for city in range(1,N+1):
        if city not in l1:
            l2.append(city)
    check(l1,l2)
    for city in range(idx,N+1):
        DFS(city+1, l1+[city])    

for i in range(1,N+1):
    DFS(i,[i])
    
# for p in range(1, 1+N//2):
#     comb = combinations([i for i in range(1,N+1)], p )
#     comb = list(comb)
#     for c in comb:
#         l1 ,l2 = [],[]
#         for i in range(1,N+1):
#             if i in c :
#                 l1.append(i)
#             else:
#                 l2.append(i)
#         check(l1,l2)
if answer == INF: print(-1)
else: print(answer)