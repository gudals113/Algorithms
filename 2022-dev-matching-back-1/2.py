# def solution(grid):
#     answer = -1
#     N = len(grid)
#     M = len(grid[0])
    
#     G=[[0 for _ in range(M)]for _ in range(N)]
#     for i in range(N):
#         for j in range(M):
#             if grid[i][j]=='a':
#                 G[i][j]=1
                
#             elif grid[i][j]=='b':
#                 G[i][j]=2
                
#             elif grid[i][j]=='c':
#                 G[i][j]=3
#     sol = 0
    
#     def check(G):
#         count0=0
#         count1=0
#         count2=0
        
#         for i in range(N):
#             for j in range(M):
#                 if visited[i][j]
    
            
    
#     def DFS(x,y):
#         if x==N-1 and y==M:
#             print(G)
#             check(G)
#             return
#         if x<N-1 and y==M:
#             x+=1
#             y=0
        
#         if G[x][y]==0:
#             G[x][y]=1
#             DFS(x,y+1)
#             G[x][y]=0   
        
#             G[x][y]=2
#             DFS(x,y+1)
#             G[x][y]=0
            
#             G[x][y]=3
#             DFS(x,y+1)
#             G[x][y]=0 
        
#         else:
#             DFS(x,y+1)
        
#     DFS(0,0)      
#     return answer

# solution(["??b", "abc", "cc?"])

