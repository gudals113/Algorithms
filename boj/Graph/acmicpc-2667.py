from collections import deque
N=int(input())
apt=[[0 for _ in range(N)]for _ in range(N)]
visited=[[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    line=input()
    for j in range(N):
        apt[i][j]=int(line[j])


dx=[0,0,-1,1]
dy=[-1,1,0,0]

def BFS(i,j):
    tmp=1
    q= deque([[i,j]])
    while (q):
        x,y=q.popleft()
        
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]

            if 0<=nx<N and 0<=ny<N and apt[nx][ny]==1 and visited[nx][ny]==0:
                visited[nx][ny]=1
                q.append([nx,ny])
                tmp+=1           
    return tmp

ans=[]
for i in range(N):
    for j in range(N):
        if apt[i][j]==1 and visited[i][j]==0:
            visited[i][j]=1
            sol=BFS(i,j)
            ans.append(sol)


ans=sorted(ans)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])
