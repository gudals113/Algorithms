N, M , H = map(int,input().split())

#visitex[x][y] x번째 세로줄 y번쨰 가로 연결
# 1-indexed
visited = [ [0 for _ in range(H+1)] for _ in range(N+2)]

for _ in range(M):
    a,b = map(int,input().split())
    #b to b+1번 세로줄 a번째 가로줄에서 연결
    visited[b][a]=1

candidate=[]
for i in range(1,N+1):
    for j in range(1,H+1):
        if visited[i][j]==0 and visited[i-1][j]==0 and visited[i+1][j]==0 :
            candidate.append([i,j])

def check():
    for i in range(1,N+1) :
        now = i
        sero = visited[now]
        left_sero = visited[now-1]

        for j in range(1,H+1):
            if left_sero[j]==1:
                now -=1
                sero = visited[now]
                left_sero= visited[now-1]
            
            elif sero[j] == 1:
                now +=1
                sero = visited[now]
                left_sero = visited[now-1]
            
        if now != i:
            return False
        
    return True

sol = 4

def DFS(idx,tmp):
    global sol, visited, ans
    
    if len(candidate)==idx or tmp>=sol:
        return False
    if check():
        sol = min(sol,tmp)
        return True
    
    x = candidate[idx][1]
    y= candidate[idx][0]

    rst = DFS(idx+1, tmp)  
  
    if visited[y-1][x]==0 and visited[y][x]==0 and visited[y+1][x]==0:
        visited[y][x]=1
        DFS(idx+1,tmp+1)
        visited[y][x]=0
        
             
DFS(0,0) 
if sol ==4:
    print(-1)
else:
    print(sol)      
    