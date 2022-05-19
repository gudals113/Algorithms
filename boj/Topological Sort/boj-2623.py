#음악프로그램 (topological sort) sol220516
#1. 그냥 구현

# from collections import deque
# N, M = map(int,input().split())
# G = [ deque() for _ in range(N+1)]
# for _ in range(M):
#     order = list(map(int, input().split()))
    
#     for i in range(2,len(order)):
#         G[order[i]].append(order[i-1])
        
# visited= [0 for _ in range(N+1)]
# answer = []
# for _ in range(N):
#     for i in range(1,N+1):
#         if visited[i]==0:
#             if len(G[i])==0 : 
#                 visited[i]=1
#                 answer.append(i)
#             else:
#                 while G[i] :
#                     pre = G[i].popleft()
                    
#                     if visited[pre]==0:
#                         G[i].append(pre)
#                         break
                    
#                 if len(G[i])==0 : 
#                     visited[i]=1
#                     answer.append(i)

# if len(answer)==N:
#     for i in range(N):
#         print(answer[i])

# else:
#     print(0)

#inDegree 개수 BFS
from collections import deque
N, M = map(int, input().split())
inDegree = [0 for _ in range(N+1)]
G=[ [] for _ in range(N+1) ]
G2 = [ []  for _ in range(N+1)]
for _ in range(M):
    order = list(map(int, input().split()))
    
    for i in range(2,len(order)):
        G[order[i]].append(order[i-1])
        G2[order[i-1]].append(order[i])
     
q= deque() 
for idx in range(1,N+1):
    inDegree[idx] = len(G[idx])
    if inDegree[idx]==0:
        q.append(idx)
         
answer = []        
while q:
    pre = q.popleft()
    answer.append(pre)
    for next in G2[pre]:
        inDegree[next]-=1
        
        if inDegree[next]==0:
            q.append(next)

if len(answer)!= N:
    print(0)
else:
    for i in range(N):
        print(answer[i])        
            
