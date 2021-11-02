#백준 11053 가장 긴 증가하는 부분 수열 LCS
N=int(input())
arr = list( map(int, input().split()) )

dp=[1 for _ in range(N)]

for i in range(1,N):
    
    for j in range(i):
        if arr[j]<arr[i]:
            
            dp[i]= max(dp[j]+1, dp[i])
            
print(max(dp))