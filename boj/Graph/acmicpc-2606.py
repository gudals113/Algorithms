N= int(input())
M = int(input())

visited = [ 0 for _ in range(N+1)]
lab = [ [] for _ in range(N+1) ]
for i in range(M):
    u,v = map(int, input().split())
    lab[u].append(v)
    lab[v].append(u)
    

sol = 0
visited[1]=1
def DFS(i):
    global sol
    for connect in lab[i]:
        if visited[connect] == 0:
            visited[connect] =1
            sol+=1
            DFS(connect)    
    
        
    
DFS(1)
# print(visited)
print(sol)