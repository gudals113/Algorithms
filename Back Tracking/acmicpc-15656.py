#N과M (7)

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
        ans.append(arr[i])
        DFS()
        ans.pop()

# DFS()

# def nDFS(index):
#     global ans
#     if len(ans)==M:
#         print(' '.join(map(str, ans)))
#         return
    
#     if index==N:
#         return
    
    
#     ans.append(arr[index])
#     nDFS(index+1)
#     ans.pop()
    
#     nDFS(index+1)   
    
# nDFS(0)