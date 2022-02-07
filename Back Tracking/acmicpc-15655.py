#15655 for말고 두가지로 나눠 푸는게 더 빠르다.  for은 O(n!) 이 되는건가? 두가지는 O(2**n)

#N과M (6)
N, M = map(int, input().split())
arr=list( map(int, input().split()) )
arr.sort()

ans=[]
# def DFS(index):
#     global ans
    
    
#     if len(ans)==M:
#         print(' '.join(map(str, ans)))
#         return
    
#     for i in range(index, N):
#         ans.append(arr[i])
#         DFS(i+1)
#         ans.pop()

# DFS(0)


def nDFS(index):
    global ans
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    
    if index==N:
        return
    
    
    ans.append(arr[index])
    nDFS(index+1)
    ans.pop()
    nDFS(index+1)   
nDFS(0)