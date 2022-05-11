N = int(input())
S = list(map(int, input().split()))
S.sort()

dp = [0 for _ in range(2000000)]

def DFS(idx,num):
    global dp
    dp[num]=1
    
    if idx == N:
        return

    if not visited[idx] :
        visited[idx]=1
        DFS(idx+1, num+S[idx])
        visited[idx]=0
    DFS(idx+1, num)
    
        
visited=[0 for _ in range(N)]        
DFS(0,0)

# print(dp)
sol=0
for i in range(1,2000001):
    if dp[i]==0:
        sol = i
        break      

print(sol)