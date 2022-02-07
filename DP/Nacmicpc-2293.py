#동전1 9084번과 동일

N,K = map(int, input().split())
dp = [0 for _ in range(K+1)]
coin=[]
for i in range( N) :
    coin.append(int(input()))
    
dp[0]=1
for j in (coin) : 
    for i in range(1,K+1):
        if i-j>=0:
            dp[i] += dp[i-j]
print(dp[K])