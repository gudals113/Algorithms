N, M = map(int, input().split())
arr=list( map(int, input().split()) )
arr.sort()

ans=[]
def DFS():
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(N):
        if ans==[] or arr[i] >= ans[-1]:
            ans.append(arr[i])
            DFS()
            ans.pop()
DFS()