#백준 15988번 1,2,3 뭐 (dp)


dp = [-1 for _ in range(1000000)]
dp[0] = 1
for i in range(1, 1000000):

    if i == 1:
        dp[i] = 2
    elif i == 2:
        dp[i] = 4

    else:
        dp[i] =( dp[i-1] + dp[i-2] + dp[i-3] )% 1000000009


T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N-1])
