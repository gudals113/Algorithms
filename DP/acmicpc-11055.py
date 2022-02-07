N=int(input())
arr=list(map(int, input().split()))
dp=[ e for e in (arr)  ]

for i in range(N):
    tmp=0
    for j in range(i, -1,-1):
        
        if arr[j] < arr[i] :
            tmp=max(tmp,dp[j])
        
    dp[i]+=tmp
        
print(max(dp))
