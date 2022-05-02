#비숍 백트래킹
N = int(input())
G=[ ]
visited = [ [-1 for _ in range(N)] for _ in range(N) ]
for _ in range(N):
    G.append(list(map(int, input().split())))

def check(x,y):
    global visited
    for i in range(1,x+1):
        if y-i<0:
            break
        
        if visited[x-i][y-i]==1:
            return False
    
    for i in range(1,x+1):
        if y+i>=N:
            break
        if visited[x-i][y+i]==1:
            return False
        
    return True

def odd_DFS(idx,count):
    global odd_sol
    global visited
    
    if idx >=N**2:
        return count
    
    x=idx//N 
    y=idx%N 
    
    tmp = odd_DFS(idx+2, count)
    odd_sol = max(odd_sol, tmp)
    
    if G[x][y]==1:
        if check(x,y)==True:
            
            visited[x][y] = 1
            
            tmp = odd_DFS(idx+2, count+1)            
            odd_sol = max(odd_sol, tmp ) 
            
            visited[x][y] = -1
    return count

def even_DFS(idx,count):
    global even_sol
    global visited
    
    if idx >=N**2:
        return count
    
    x=idx//N 
    y=idx%N 
    
    if y == N-1:
        tmp = even_DFS(idx+1, count)
    elif y == N-2:
        tmp = even_DFS(idx+3, count)
    else:
        tmp= even_DFS(idx+2,count)    
        
    even_sol = max(even_sol, tmp)
    
    if G[x][y]==1:
        if check(x,y)==True:
            
            visited[x][y] = 1
            
            if y ==N-1:
                tmp = even_DFS(idx+1, count+1)
            elif y == N-2:
                tmp = even_DFS(idx+3, count+1)
            else:
                tmp= even_DFS(idx+2,count+1)             
            even_sol = max(even_sol, tmp ) 
            
            visited[x][y] = -1
    return count

            
sol=0

if N%2==1:
    odd_sol = 0
    odd_DFS(0,0)
    sol+=odd_sol

    odd_sol=0
    odd_DFS(1,0)
    sol+=odd_sol
else:
    even_sol=0
    even_DFS(0,0)
    sol+=even_sol
    
    even_sol=0
    even_DFS(1,0)
    sol+=even_sol
    
print(sol)


    
        