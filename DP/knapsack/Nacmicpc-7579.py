#앱, 0-1 냅색 알고리즘 
# 제출 안함
#M바이트 이상을 최소 코스트로 확보

N, M = map(int, input().split())
memory = [0]+list( map(int, input().split()) )
cost = [0]+list(map(int, input().split()))
result = sum(cost)+1

dp = [ [0 for _ in range(sum(cost)+1)] for _ in range(N+1)]
# dp[i][j] i번쨰 앱까지 j코스트로 최대 확보할 수 있는 바이트

for i in range(1, N+1) : 
    m = memory[i]
    c = cost[i]
    for j in range(1, sum(cost)+1) :
        if j < c :
            dp[i][j] = dp[i-1][j]
        
        else:
            
            dp[i][j] = max(dp[i-1][j-c] + m, dp[i-1][j])
        
        if dp[i][j] >= M :
            result = min(result, j)

print(result)