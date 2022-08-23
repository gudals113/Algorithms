#단절선 , ? ,try220701
#이거 못풀겠네.. 
V,E = map(int, input().split())
G = [ [] for _ in range(V+1) ]
for _ in range (E):
    
    u,v =map(int, input().split())
    G[u].append(v)
    G[v].append(u)
    
visited= [ 0 for _ in range(V+1)]
sol=[]
def DFS(before,node):
    global sol
    
    print(node)
    
    for next in G[node]:
        if next==before:
            continue
        
        
        
        if visited[next]==0 :

            visited[next] = visited[node]+1
            
            if DFS(node,next) == True :
                sol.append([node, next])
           
                
        elif visited[next]<visited[node]:
            return False
    
    return True
   
visited[1]=1
DFS(0,1)
print(visited)
print(sol)          
