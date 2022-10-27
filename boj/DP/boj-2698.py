# 인접한 비트의 개수
# 정말 괜찮은 DP 문제
# 220916

# dp[x][y] = x자리에서 1이 y개 인접하고 0으로 끝나는 경우 /1으로 끝나는 경우

dp = [ [ [0,0] for _ in range(101)] for _ in range(101)]


dp[1][0][0] = 1 #0 
dp[1][0][1] = 1 #1

for k in range(2,101):
    for i in range(0,k):
        dp[k][i][0] = dp[k-1][i][0] + dp[k-1][i][1]
        
        if i==0:
            dp[k][0][1] = dp[k-1][0][0]
        else:
            dp[k][i][1] = dp[k-1][i][0] + dp[k-1][i-1][1]


T = int(input())
for _ in range(T):
    n,k = map(int,input().split())
    print(sum(dp[n][k]))

