#N과M (5)
N, M = map(int, input().split())
arr=list( map(int, input().split()) )
arr.sort()

ans=[]
def DFS():
    global ans
    
    
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(N):
        if arr[i] not in ans:
            ans.append(arr[i])
            DFS()
            ans.pop()

DFS()





    

    