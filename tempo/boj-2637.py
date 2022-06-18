# from collections import deque
# N = int(input())
# M = int(input())
# G = [[]for _ in range(N+1)]
# for _ in range(M):
#     x,y,z = map(int,input().split())
#     G[x].append([y,z])

# dict =[0 for _ in range(N+1)]
# q = deque([[N,1]])

# while q :
#     now , now_need= q.popleft()
#     #now 1개 만들기 위한 part의 개수 part_need, now_need 개 만들기 위해서는 part가  now_need*part_need개 필요하다.
#     if len(G[now])==0:
#         dict[now]+= now_need 
#     else:
#         for part, part_need in G[now]:
#             q.append([part, now_need*part_need])

# for i in range(1,N+1):
#     if dict[i]!=0:
#         print(i, dict[i])

from collections import deque
N = int(input())
M = int(input())
G = [[0 for _ in range(N+1) ]for _ in range(N+1)]
for _ in range(M):
    x,y,z = map(int,input().split())
    G[y][x]=z
    



            
