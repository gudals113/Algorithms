#열쇠 bfs, sol 220628
from collections import deque
T=int(input())
sol=[]
for _ in range(T):
    H,W = map(int, input().split())
    G=[ ['.' for _ in range(W+2)]for _ in range(H+2)]
    for i in range(1,H+1):
        l = input()
        for j in range(1,W+1):
            G[i][j]=l[j-1]

    key = {}
    l = input()
    for word in l :
        key[word]=1
        
    visited = [ [ 0 for _ in range(W+2)] for _ in range(H+2) ]
    q=deque([[0,0]])
    visited[0][0]=1
    answer=0

    while q :
        x,y = q.popleft()
        
        for nx,ny in ([x+1,y],[x-1,y],[x,y+1],[x,y-1]):
            if 0<=nx<H+2 and 0<=ny<W+2 and not visited[nx][ny] : 
                if G[nx][ny] == '.':
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    
                elif G[nx][ny] == '$' :
                    answer+=1
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    G[nx][ny]='.'
                    
                #소문자(key)인 경우
                elif 97<= ord(G[nx][ny]) <=122 :

                    key[G[nx][ny]] = 1
                    visited[nx][ny]=1
                    q.append([nx,ny])
                    G[nx][ny]='.'
                    visited = [ [ 0 for _ in range(W+2)] for _ in range(H+2) ]

                #대문자인(door) 경우
                elif 65<= ord(G[nx][ny]) <=90 : 
                    need = chr(ord(G[nx][ny]) + 32 )
                    if need in key :
                        visited[nx][ny]=1
                        q.append([nx,ny])
                        G[nx][ny]='.'
                
    sol.append(answer)

for i in range(T):
    print(sol[i])