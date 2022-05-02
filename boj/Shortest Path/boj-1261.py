#알고스팟
# from collections import deque
# M,N = map(int,input().split())
# G=[[0 for _ in range(M)]for _ in range(N)]
# for i in range(N):
#     l = input()
#     for j in range(M):
#         G[i][j]=int(l[j])

# visited = [ [-1 for _ in range(N)] for _ in range(M) ]
# def BFS():
#     q = deque([[0,0,0]])
#     visited[0][0]=0
#     while q :
#         x,y, cost = q.popleft()
#         for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
#             if 0<=nx<N and 0<=ny<M:
#                 if G[nx][ny] == 0 :
#                     if visited[nx][ny]>cost or visited[nx][ny]==-1:
#                         visited[nx][ny]=cost
#                         q.append([nx,ny,visited[nx][ny]])

#                 else:
#                     if visited[nx][ny]>cost+1 or visited[nx][ny]==-1:
#                         visited[nx][ny]=cost+1
#                         q.append([nx,ny,visited[nx][ny]])
# BFS()
# print(visited[N-1][M-1])


from heapq import heappop, heappush
M,N = map(int,input().split())
G=[[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(M):
        G[i][j]=int(l[j])

visited = [ [-1 for _ in range(M)] for _ in range(N) ]
def BFS():
    q = []
    heappush(q, [0,0,0])
    visited[0][0]=1
    
    while q :
        cost, x,y = heappop(q)
        if x==N-1 and y==M-1:
            print(cost)
            break
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<N and 0<=ny<M:
                if visited[nx][ny]==-1:
                    if G[nx][ny]==1:
                        visited[nx][ny]=cost+1
                        heappush(q, [cost+1, nx,ny])
                    else:
                        visited[nx][ny]=cost
                        heappush(q, [cost, nx, ny])

BFS()
# print(visited[N-1][M-1])