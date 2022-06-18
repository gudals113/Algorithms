N, M, H = map(int, input().split())
dp= [ [0 for _ in range(2002)] for _ in range(N+1) ]

for i in range(1,N+1):
    L = list(map(int, input().split()))     

    for k in range(1,1001):
        if dp[i-1][k] != 0 :
            dp[i][k] = dp[i-1][k]
    
    
    for j in range(len(L)):
        block=L[j]
        dp[i][block] += 1
        
    for j in range(len(L)): 
        block=L[j]    
        
        for k in range(1001):
            if dp[i-1][k] != 0:
                dp[i][k+block] += dp[i-1][k] 
                
    # for j in range(len(L)):
    #     block=L[j]
    #     dp[i][block] += 1
    

print(dp[N][H]%10007)
    
    