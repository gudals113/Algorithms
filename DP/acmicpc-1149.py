#백준 1149번 RGB거리(dp)
# dp=[[1,2,3,4,5,6,,,,n],[1,2,3,4,4,5,6,7,,,,n],[]]

dp=[[],[],[]]
rgb=[]
N=int(input())
for _ in range(N):
    rgb.append(list(map(int, input().split())))

dp[0].append(rgb[0][0])
dp[1].append(rgb[0][1])
dp[2].append(rgb[0][2])

for i in range(1,N):
    dp[0].append( min(dp[1][i-1], dp[2][i-1]) + rgb[i][0])
    dp[1].append( min(dp[0][i-1], dp[2][i-1]) + rgb[i][1])
    dp[2].append( min(dp[0][i-1], dp[1][i-1]) + rgb[i][2])

print( min( dp[0][N-1], dp[1][N-1], dp[2][N-1] ) )

# 시간 줄이려면 