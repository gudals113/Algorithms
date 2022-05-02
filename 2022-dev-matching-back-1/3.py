def solution(n, edges, k, a, b):
    M = len(edges)
    
    Evisited=[0 for _ in range(M)]
    
    visited=[0 for _ in range(n)]
    tmp = [0 for _ in range(M)]
    
    def DFS(node,sum):    
      
        if node == b :
            if sum <=k:
                print(tmp)

                for i in range(M):
                    if tmp[i]==1:
                        Evisited[i]+=1
                
            return
        for i in range(M):
            u,v = edges[i][0], edges[i][1]
        
            if node==u :
                
                if visited[v]==0:
                    visited[v]=1
                    tmp[i]=1
                    
                    DFS(v,sum+1)
                    
                    tmp[i]=0
                    visited[v]=0
                    
            elif node==v:
                
                if visited[u]==0:
                    visited[u]=1
                    tmp[i]=1
                    
                    DFS(u,sum+1)
                    
                    tmp[i]=0
                    visited[u]=0
            
                
                            
    visited[a]=1
    DFS(a,0)

    sol = M
    for i in range(M):
        if Evisited[i]==0:
            sol-=1
    

        
    return sol


