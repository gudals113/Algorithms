# boj-3109.py
# 빵집 
# sol 220805 10:05-
# greedy, DFS

N,M = map(int, input().split())
G = [[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    l = input()
    for j in range(M):
        if l[j]=='x':
            G[i][j]=1

def DFS(x,y):
    print(x,y)
    if y==M-1 :
        visited[x][y]=1
        return True
    
    for nx,ny in ( [x-1,y+1],[x,y+1],[x+1,y+1] ) :
        if 0<=nx<N and 0<=ny<M  and not visited[nx][ny] and G[nx][ny]==0 : 
            rst = DFS(nx,ny)
            visited[nx][ny]=1
            if rst==True:
                return True
    return False
    
    
answer = 0 
visited=[[0 for _ in range(M)]for _ in range(N)]  
for x in range(N):
    if DFS(x,0)== True:
        answer+=1
print(answer)