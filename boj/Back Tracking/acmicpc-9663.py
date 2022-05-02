# N - queen
N = int(input())
chess=[-1 for _ in range(N)]
visited=[-1 for _ in range(N)]
ans=0
def queen(x,placed):
    global ans
    
    if placed == N :
        ans+=1
        return 
    
    if x == N :
        return
    
    for i in range(N):
        if visited[i] == -1 : 
            if check(x, i) == True:
                visited[i], chess[x] = 1,i
                queen(x+1,placed+1)
                visited[i], chess[x] = -1, -1
                
def check(x, idx):   
    for i in range(N):
        if chess[i] ==-1:
            continue
        if abs(x-i) == abs(idx-chess[i]) :
            return False
    
    return True

queen(0,0)
print(ans)
