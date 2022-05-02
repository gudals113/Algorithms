from collections import deque


N = int(input())
G = [ [0] ]
for i in range(N):
    G.append(list(map(int,input().split())))

M=int(input())    
start=list(map(int,input().split()))


visited=[-1 for _ in range(N+1)]

def check(node, time):
    rumor=0
    for next in G[node]:
        if next!=0:
            if visited[next] !=-1 and visited[next]<=time:
                rumor+=1
            else:
                rumor-=1
    
    if rumor >=0:
        return True            
                
    
def BFS():
    q=deque([])
    for s in start:
        q.append(s)
        visited[s]=0
    
    while q :
        now = q.popleft()
             
        for next in G[now]:
            if next!=0 :
                if visited[next]==-1 :
                    
                    if check(next, visited[now])==True:
                        visited[next]= visited[now]+1
                        q.append(next)
BFS()
         
print(*visited[1:])                    
