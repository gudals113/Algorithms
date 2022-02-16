#동전(dp)
T= int(input())
for _ in range(T):
    
    N = int(input())
    coin = list(map(int, input().split()))
    target = int(input())
    
    dp= [0 for _ in range(target+1)]
    dp[0]=1
    
    for e in coin:
        for i in range(1,target+1):
            if i-e>=0 :
                dp[i] += dp[i-e]
    print(dp[target])