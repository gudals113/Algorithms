#꽃길

from itertools import combinations
N = int(input())
price=[]
for _ in range(N):
    price.append( list( map(int, input().split()) ) )

dx=[0,0,0,1,-1]
dy=[0,1,-1,0,0]
def DFS(comb):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    total = 0
    
    for seed in comb:
        tmp = 0
        x= seed//N
        y= seed%N

        for i in range(5):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0 :
                visited[nx][ny]=1
                tmp += price[nx][ny] 
            else:
                return 3000
        
        total += tmp
        
    return total

tmp=3000
idx = [i for i in range(N**2)]
for i in combinations(idx, 3):
    tmp = min(tmp, DFS(i))
print(tmp)