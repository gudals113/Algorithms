#N과M (1)
N,M = map(int, input().split())
arr=[]

ans=0   

def DFS(ans):
    global arr,sol
    
    if ans==M:
        print(' '.join(map(str, arr)))
        return
        
        
        
    for i in range(1, N+1):
        if i not in arr:
            arr.append(i)
            DFS(ans+1)
            arr.pop()

DFS(0)
