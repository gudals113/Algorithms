N= int(input())
# G = [ [0 for _ in range(N)] for _ in range(N)]
chess = [0 for _ in range(N)]
visited=[ 0 for _ in range(N)] 

def check(x,y):
    
    for i in range(x):
        if chess[i]==y:
            return False
        
        if abs(x-i) == abs(y-chess[i]) :
            return False
        
    return True
    


sol= 0
def DFS(x):
    global sol
    if x == N :
        sol+=1
        return 
    
    for y in range(N):
        if visited[y]!=1:
            if check(x,y):
            
                visited[y]=1
                chess[x]=y
                DFS(x+1)
                visited[y]=0
                chess[x]=0
    return

DFS(0)
print(sol)