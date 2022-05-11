#줄세우기
#LIS

N = int(input())
L = [ int(input()) for _ in range(N)]

dp = [ 1 for _ in range(N)]
for i in range(1,N):
    for j in range(i-1,-1,-1):
        if L[j] < L[i]:
            dp[i] = max(dp[i], dp[j]+1)
        
# print(dp)
print(N - max(dp))