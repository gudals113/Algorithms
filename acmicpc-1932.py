# 백준 1932 RGB 거리

N = int(input())
trgl = []
for _ in range(N):
    line = list(map(int, input().split()))
    trgl.append(line)

dp = []
for i in range(N):
    dp.append([0]*(i+1))
dp[0][0] = trgl[0][0]

for i in range(1, N):
    #각 단계에 i+1개 갱신
    dp[i][0] = dp[i-1][0] + trgl[i][0]
    dp[i][i] = dp[i-1][i-1]+trgl[i][i]

    for j in range(1, i):
        dp[i][j] = trgl[i][j] + max(dp[i-1][j], dp[i-1][j-1])


# print(dp)
print(max(dp[N-1]))

# for i in range(1, 2):
    # print(i)