# 불
# sol 220802 10:31-
# BFS

from collections import deque
sol=[]
T = int(input())
for _ in range(T):
    W,H = map(int, input().split())
    G = [ ['.' for _ in range(W)] for _ in range(H) ]
    mx,my = 0,0
    F=deque()
    for i in range(H) :
        l = input()
        for j in range(W):
            G[i][j] = l[j]
            
            if l[j]=='*':
                F.append([i,j])
            if l[j]=='@':
                mx,my = i,j
                

    fireVisited=[[ -1 for _ in range(W)]for _ in range(H)]
    # 불 언제 옮겨 붙는지 BFS
    
    q= deque()
    for x,y in F:
        fireVisited[x][y] = 0
        q.append([x,y])
        
    while q :
        ax,ay = q.popleft()
        for nx,ny in ([ax+1,ay],[ax-1,ay],[ax,ay+1],[ax,ay-1]):
            if 0<=nx<H and 0<=ny<W and (G[nx][ny]=='@' or G[nx][ny]=='.'):
                if fireVisited[nx][ny]==-1 :
                    fireVisited[nx][ny] = fireVisited[ax][ay]+1
                    q.append([nx,ny])

    

    q=deque([[mx,my]])
    visited=[[ -1 for _ in range(W)]for _ in range(H) ]
    visited[mx][my] = 0
    answer = "IMPOSSIBLE"
    while q:
        x,y = q.popleft()
        time = visited[x][y]
        if x==0 or x==H-1 or y==0 or y==W-1:
            answer =time+1
            break
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<H and 0<=ny<W and G[nx][ny]=='.' and visited[nx][ny] ==-1:
                if fireVisited[nx][ny]>time+1 or fireVisited[nx][ny]==-1 :
                    visited[nx][ny]=time+1
                    q.append([nx,ny])
                    
    sol.append(answer)
    
for a in sol:
    print(a)