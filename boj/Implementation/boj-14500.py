#테트로미노 구현
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G=[]
for _ in range(N):
    G.append(list(map(int, input().split())))

def DFS(x,y, count, sum):
    global sol
    
    if count == 3:
        sol = max(sol, sum)
        return True
    
    for nx,ny in ([x+1,y], [x,y+1],[x-1,y],[x,y-1]):
        if nx>=0 and nx<N and ny>=0 and ny<M :
            if not visited[nx][ny]:
                visited[nx][ny]=1
                DFS(nx, ny, count+1, sum+G[nx][ny])
                visited[nx][ny]=0
    
    
def FUCK(x,y):
    global sol
    tmp = 0
    #ㅗ,ㅜ
    for nx,ny in ([x,y],[x,y+1], [x,y+2]):
        if nx>=0 and nx<N and ny>=0 and ny<M :
            tmp+=G[nx][ny]
        else:
            tmp = 0
            break
        
    if tmp !=0:
        add=0
        
        for nx,ny in ([x-1,y+1],[x+1,y+1]):
            if nx>=0 and nx<N and ny>=0 and ny<M :
                add=max(add,G[nx][ny])     
        
        if add !=0:
            sol = max(sol,tmp+add)    
    
    #ㅏ,ㅓ
    tmp=0
    for nx,ny in ([x,y],[x+1,y], [x+2,y]):
        if nx>=0 and nx<N and ny>=0 and ny<M :
            tmp+=G[nx][ny]
        else:
            tmp = 0
            break
   
    if tmp!=0:
        add=0
        for nx,ny in ([x+1, y-1],[x+1, y+1]):
            
            if nx>=0 and nx<N and ny>=0 and ny<M :
                add=max(add,G[nx][ny])
        if add !=0:
            sol = max(sol,tmp+add)    
    return
            
                        
sol=0
visited=[ [0 for _ in range(M)] for _ in range(N) ]
for x in range(N):
    for y in range(M):
        visited[x][y]=1
        DFS(x,y, 0, G[x][y])
        visited[x][y]=0
        FUCK(x,y)

print(sol)

# def tetromino(x,y):
#     sol=[]
#     tmp=G[x][y]
    
#     #가로 직선
#     for nx,ny in ([x,y+1],[x,y+2],[x,y+3]) :
#         if ny<M :
#             tmp+=G[nx][ny]
#         else:
#             tmp=0
#             break
        
#     sol.append(tmp)
#     tmp=G[x][y]
    
#     #네모
#     for nx,ny in ([x+1,y], [x+1,y], [x+1,y+1]) :
#         if nx<N and ny<M :
#             tmp+=G[nx][ny]
#         else:
#             tmp=0
#             break
#     sol.append(tmp)
#     tmp=G[x][y]
    
#     #ㄴ자
#     for nx,ny in ([x+1,y], [x+2,y], [x+2,y+1]) :
#         if nx<N and ny<M :
#             tmp+=G[nx][ny]
#         else:
#             tmp=0
#             break
#     sol.append(tmp)
#     tmp=G[x][y]
    
#     #두번꺽
#     for nx,ny in ([x+1,y], [x+1,y+1], [x+2,y+1]) :
#         if nx<N and ny<M :
#             tmp+=G[nx][ny]
#         else:
#             tmp=0
#             break
#     sol.append(tmp)
#     tmp=G[x][y]
    
#     #ㅜ
#     for nx,ny in ([x,y+1], [x+1,y+1], [x,y+2]) :
#         if nx<N and ny<M :
#             tmp+=G[nx][ny]
#         else:
#             tmp=0
#             break
#     sol.append(tmp)
#     tmp=G[x][y]
    
#     return max(sol)






# ans = 0
# for _ in range(4):
#     N,M =n,m
#     G=g
    
    
    
#     for x in range(N) :
#         for y in range(M):
#             result = tetromino(x,y)
#             ans = max(ans, result)
            
# print(ans)