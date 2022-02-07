#N과M (2)
N,M = map(int, input().split())
arr=[]

def DFS(idx):
    global arr
    
    if idx == N+1:
        return 
    
    if len(arr)==M:
        print(' '.join(map(str, arr)))
        return
        
        
        
    for i in range(idx, N+1):
        if i not in arr:
            arr.append(i)
            DFS(i)
            arr.pop()

DFS(1)