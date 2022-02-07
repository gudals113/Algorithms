#기업투자( 0-1 냅색 알고리즘)
N, M = map(int, input().split())
company = [[0 for _ in range(M+1)]]
for i in range(N):
    company.append(list(map(int, input().split())))
# 최대 이익 2**31이다. 이게 dp의 값으로 저장되어야 한다.

# i 번째 기업까지 선택 시 최대 이익을 갱신해가볼까. 금액을 cost로 생각하자

dp=[[ [0,0] for _ in range(N+1)] for _ in range(M+1)]
for i in range(1,M+1) : 
    
    for j in range(1, N+1):
        # i번째 기업까지 j원 투자해서 얻는 이익 = max(
            # i-1번째 기업까지 j원 투자해서 얻는 이익
            # i-1번쨰 기업까지 j-1원 투자해서 얻는 이익 + i번째 기업이 1원 투자해서 얻는 이익
            # i-1번째 기업까지 j-2원 투자해서 얻는 이익 + i번째 기업이 2원 투자해서 얻는 이익
            # i-1번째 기업까지 0원 투자해서 얻는 이익 + i번쨰 기업이 j(N)원 투자해서 얻는 이익    
            
            # k=0에서 j까지 루프
            # i-1번째 기업까지 j-k원 투자 이익, i번쨰 기업이 k원 투자 이익    
        # )
        
        for k in range(0, j+1):
            tmp1 = dp[i][j][0]
            tmp2 = dp[i-1][j-k][0] + company[k][i]
            
            if tmp1>=tmp2:
                #dp[i][j]=tmp1
                #ans[i-1]=ans[i-1]
                pass
            else:
                dp[i][j][0] = tmp2
                dp[i][j][1] = k

tmp = N
ans=[0 for _ in range(M)]

for i in range(M):
    # if tmp<=0 :
    #     break
    
    used = dp[M-i][tmp][1]
    ans[M-1-i]=used
    
    tmp = tmp-used

print(dp[M][N][0])
print(*ans)