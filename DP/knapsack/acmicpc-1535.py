#안녕, cost 100까지 최대 행복 구하기
N = int(input())
L = [0]+list( map(int, input().split()))
J = [0]+list(map(int, input().split()))
SOL = 0
# dp [i][j] = i번쨰 사람에게 인사했을 때 J 행복 얻을 때 코스트 / dp[i][j] = dp[i-1][j - happy ] + cost / dp[i][j] = dp[i-1][j
# dp [i][j] = dp[i-1][j-cost] + happy, dp[i-1][j]

dp=[ [0 for _ in range(101)] for _ in range(N+1) ]

for i in range(1,N+1):
    lose = L[i]
    joy = J[i]
    
    for j in range(1, 101) :
        dp[i][j] = dp[i-1][j]
        
        if j-lose>=0:
            dp[i][j] =max(dp[i][j], dp[i-1][j-lose] + joy )
        
    SOL = max(SOL, dp[i][99])

# print(dp)
print(SOL)
            
