#평범한 배낭2
N, M = map(int, input().split())
stuff = [[0,0,0]]
# costSum = 0
for _ in range(N) :
    line = list(map(int, input().split()))
    # costSum += line[0] * line[2]
    stuff.append(line)
    
# stuff[]  = 무게, 만족도, 개수
dp=[ [ 0 for _ in range(M+1)] for _ in range(N+1) ]

# 모든 물품에 대하여 루프
for i in range(1, N+1):
    cost = stuff[i][0]
    bnf = stuff[i][1]
    num = stuff[i][2]
    
    
    #최대무게 부터 무게1까지 에 대하여 루프 
    for j in range(M,0,-1) :
        dp[i][j]= dp[i-1][j]
        maxnum=num
        
        
        #i번째 물건 사용할 수 있는만큼 루프 돌리지 말고 만약에 i번쨰 물건 사용하는데 감소하면 바로 브렠 모든 경우 볼 필요 없다
        if j <= num * cost:
            maxnum = j//cost    
            
        for k in range(maxnum,0,-1):
            if j>=cost*k :

                dp[i][j] = max(dp[i][j], dp[i-1][j-cost*k]+bnf*k)          
                
                
print(dp[N][M])