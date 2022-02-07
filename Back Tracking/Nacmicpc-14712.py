#넴모넴모(easy) , backtraking

N, M = map(int, input().split())

arr=[ [0 for _ in range(M+1)] for _ in range(N+1) ]
ans=0
def DFS(index_x,index_y):
    global ans
    
    if index_x==N and index_y == M+1 :
        ans+=1
        return
    
    
    if index_y ==M+1:
        index_x+=1
        index_y=1
    
    DFS(index_x, index_y+1)
    
    if arr[index_x -1][index_y]==0 or arr[index_x][index_y-1]==0 or arr[index_x-1][index_y-1]==0:
        arr[index_x][index_y]=1
        DFS(index_x, index_y+1)    
        arr[index_x][index_y]=0
    
DFS(1,1)
print(ans)
    
