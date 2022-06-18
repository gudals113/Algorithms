C,N = map(int,input().split())
candidate = []
for _ in range(N):
    cost, benefit = map(int,input().split())
    candidate.append([cost/benefit,cost, benefit])

candidate.sort(key=lambda x: (x[0], x[2] ))
INF = float('inf')
dp = [ [INF for _ in range(1001)]  for _ in range(N)]

_, cost, benefit = candidate[0]

for i in range(1001):
    if i>benefit:
        cost+=candidate[0][1]
        benefit+=candidate[0][2]
        
    dp[0][i] = cost

for i in range(1,N):
    _, cost, benefit = candidate[i]
    
    for j in range(1001):
        dp[i][j]= dp[i-1][j]
        
        k=0
        while True:
            if j-k*benefit<=0:
                dp[i][j] = min(dp[i][j], cost*k)
                break

            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j-benefit*k] + cost*k)
                k+=1

print(dp[N-1][C])
    
    
    