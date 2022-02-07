# #부분수열의 합  백트래킹
N, S = map(int, input().split())
arr = list(map(int, input().split()))
tmp=0
sol = 0
def DFS(index):
    global tmp, sol
    if index == N :
        print(tmp, index)
        return

    if tmp + arr[index] == S:
        sol +=1

    DFS(index+1)
    
    tmp += arr[index]
    DFS(index+1)
    
    tmp -= arr[index]

DFS(0)
print(sol)



# ans = 0
# def DFS(visited, index):    

#     global ans
    
#     tmp=0
#     for j in range(N):
#         if visited[j]==1:
#             tmp+=arr[j]
    
#     if tmp==S:
#         ans+=1
    
    
#     for i in range(index, N):
#         if visited[i]==0:
#             visited[i]=1
#             DFS(visited, i)
#             visited[i]=0
            
#     return
    
# start = [0 for _ in range(N)]

# for i in range(N):
#     start[i]=1
#     DFS(start,i) 
#     start[i]=0

# print(ans)

