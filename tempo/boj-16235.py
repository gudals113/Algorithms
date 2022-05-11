from collections import deque

N,M,K = map(int,input().split())
A=[]
for _ in range(N):
    A.append(list(map(int, input().split())))

tree = [ [deque() for _ in range(N)] for _ in range(N)]
# tree=[]

nut = [[5 for _ in range(N)]for _ in range(N)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [1,0,-1,1,-1,1,0,-1]
for _ in range(M):
    x,y,z = map(int,input().split())
    tree[x-1][y-1].append(z)
    # tree.append([x-1,y-1,z])


alive = M
for _ in range(K):
    #봄
    
    toDie = []
    for x in range(N):
        for y in range(N):
            lenght = len(tree[x][y])
            for k in range(lenght):
                if tree[x][y][k] <= nut[x][y]:
                    nut[x][y]-=tree[x][y][k]
                    tree[x][y][k]+=1
                else:
                    for _ in range(k,lenght):
                        nut[x][y]+=tree[x][y].pop()//2
                        alive-=1
                    break
    




    
    for x in range(N):
        for y in range(N):
            for k in range(len(tree[x][y])):
                age = tree[x][y][k]
                if age%5==0:
                    for j in range(8) :
                        nx,ny = x+dx[j],y+dy[j]
                        if 0<=nx<N and 0<=ny<N :
                            tree[nx][ny].appendleft(1)
                            alive+=1
    
    
    for x in range(N):
        for y in range(N):
            nut[x][y]+=A[x][y]


print(alive)








