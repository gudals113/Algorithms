#피보나치 수 6 (행렬의 곱) 220503 - 220503
N = int(input())
#  1 000 000 007

dp = [0,1]

for i in range(2,N+1):
    # tmp=(dp[i-2] + dp[i-1] ) % 1000000007
    tmp=(dp[i-2] + dp[i-1] )
    dp.append(tmp)

print(dp)



