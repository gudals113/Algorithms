# RGB거리 2
# 220830
# dp
INF = float('inf')
N = int(input())
costList = [[0,0,0]]
for i in range(N):
    costList.append(list(map(int, input().split())))

answer = INF

for s in range(3):
    dp = [[INF,INF,INF]for _ in range(N+1)]
    dp[1][s] = costList[1][s]
    for h in range(2,N+1):
        dp[h][0] = min(dp[h-1][1], dp[h-1][2]) + costList[h][0]
        dp[h][1] = min(dp[h-1][0], dp[h-1][2]) + costList[h][1]
        dp[h][2] = min(dp[h-1][1], dp[h-1][0]) + costList[h][2]
    
    for e in range(3):
        if s!=e:
            answer = min(answer, dp[N][e])
print(answer)    
