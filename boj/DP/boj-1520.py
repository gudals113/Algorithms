#내리막길 (dp ) 220503
M,N = map(int,input().split())
G = []
H = 0
for _ in range(M):
    G.append(list(map(int, input().split())))
    
# visited = [[0 for _ in range(N)]for _ in range(M)]
# visited[0][0]=1
dp =[ [-1 for _ in range(N)] for _ in range(M) ]
dp[0][0] = 1
def DFS(x,y):
    if dp[x][y] != -1 :
        return dp[x][y]
    
    else:
        tmp = 0
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<M and 0<=ny<N and G[nx][ny] > G[x][y]:
                tmp += DFS(nx,ny)                
                
        dp[x][y] = tmp
        return dp[x][y]
        
        


sol = DFS(M-1,N-1)
print(sol)