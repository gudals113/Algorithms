
################################### DFS 재귀 사용해서 풀기#########################################################
# import sys
# sys.setrecursionlimit(15000)

# N=int(input())
# land= [[0 for _ in range(N)] for _ in range(N)] 
# sol=1
# #가장 높은 영역의 높이
# H=0

# #격자 생성 및 H 갱신
# for i in range(N): 
#     line = list(map(int, input().split()))

#     for j in range(N):
#         land[i][j]=line[j]
#         H=max(H,line[j])

# def DFS(x,y,h):
#     if x<0 or x>=N or y<0 or y>=N :
#             return False

#     dx=[0,0,1,-1]
#     dy=[1,-1,0,0]
#     if visited[y][x]==0 and land[y][x]>h:
#         visited[y][x]=1
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             DFS(nx, ny,h)
        
#         return True

#     return False

# for h in range(1,H):
#     visited=[[0 for _ in range(N)] for _ in range(N)] 
#     tmp=0
#     for i in range(N):
#         for j in range(N):
#             if land[i][j] > h and visited[i][j]==0:
#                 if DFS(j,i,h) == True:
#                     tmp+=1
#     sol=max(sol, tmp)
    

# print(sol)

##################################### DFS stack 사용해서 풀기 ################################################################
# N=int(input())
# land= [[0 for _ in range(N)] for _ in range(N)] 
# sol=1
# #가장 높은 영역의 높이
# H=0

# #격자 생성 및 H 갱신
# for i in range(N): 
#     line = list(map(int, input().split()))

#     for j in range(N):
#         land[i][j]=line[j]
#         H=max(H,line[j])


# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# for h in range(1,H):
#     visited=[[0 for _ in range(N)] for _ in range(N)] 
#     stack=[]
#     tmp=0
#     for i in range(N):
#         for j in range(N):

#             if land[i][j] >h and visited[i][j] ==0:
#                 stack.append([i,j])

#                 while (stack) :
#                     x,y = stack.pop()
                 
#                     if x<0 or x>=N or y<0 or y>=N:
#                         pass

#                     elif visited[x][y]==0 and land[x][y] >h:
#                         visited[x][y]=1
#                         for k in range(4):
#                             nx=x+dx[k]
#                             ny=y+dy[k]
#                             stack.append([nx,ny])

#                 tmp+=1
    
#     sol= max(sol,tmp)
# print(sol)

##################################### BFS queue 사용해서 풀기 ################################################################
# from collections import deque

# N=int(input())
# land= [[0 for _ in range(N)] for _ in range(N)] 
# sol=1
# #가장 높은 영역의 높이
# H=0

# #격자 생성 및 H 갱신
# for i in range(N): 
#     line = list(map(int, input().split()))

#     for j in range(N):
#         land[i][j]=line[j]
#         H=max(H,line[j])


# dx=[0,0,1,-1]
# dy=[1,-1,0,0]
# for h in range(1,H):
#     visited=[[0 for _ in range(N)] for _ in range(N)] 
#     q=deque([])
#     tmp=0
#     for i in range(N):
#         for j in range(N):

#             if land[i][j] >h and visited[i][j] ==0:
#                 q.append([i,j])

#                 while (q) :
#                     x,y = q.popleft()
                 
#                     if x<0 or x>=N or y<0 or y>=N:
#                         pass

#                     elif visited[x][y]==0 and land[x][y] >h:
#                         visited[x][y]=1
#                         for k in range(4):
#                             nx=x+dx[k]
#                             ny=y+dy[k]
#                             q.append([nx,ny])

#                 tmp+=1
    
#     sol= max(sol,tmp)
# print(sol)




#######################################################################DFS stack 2번째 방법#



N=int(input())
land= [[0 for _ in range(N)] for _ in range(N)] 
sol=1
#가장 높은 영역의 높이
H=0

#격자 생성 및 H 갱신
for i in range(N): 
    line = list(map(int, input().split()))

    for j in range(N):
        land[i][j]=line[j]
        H=max(H,line[j])


dx=[0,0,1,-1]
dy=[1,-1,0,0]
for h in range(1,H):
    visited=[[0 for _ in range(N)] for _ in range(N)] 
    stack=[]
    tmp=0
    for i in range(N):
        for j in range(N):

            if land[i][j] >h and visited[i][j] ==0:
                stack.append([i,j])

                while (stack) :
                    x,y = stack.pop()
                    visited[x][y]=1
                  
                    for k in range(4):
                        nx=x+dx[k]
                        ny=y+dy[k]
                        if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 and land[nx][ny] >h:
                            stack.append([nx,ny])

                tmp+=1
    
    sol= max(sol,tmp)
print(sol)