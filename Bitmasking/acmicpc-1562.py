N=int(input())

# dp[비트마스크][자릿수][끝나는수]
dp=[ [ [0 for _ in range(10)] for _ in range(N+1) ] for _ in range(1<<10) ]

for i in range(1,10):
    dp[1<<i][1][i]=1

for i in range(1, N+1):
    for j in range(10): #추가 되는 수
        for visited in range(1024): #0b 0000 0000 00 ~ 0b 1111 1111 11 
            
            if j >0:
                dp[visited | 1<<j ][i][j] += dp[visited][i-1][j-1] % 1000000000

            if j <9:
                dp[visited | 1<<j ][i][j] += dp[visited][i-1][j+1] % 1000000000

        

sol=0
for i in range(10):
    sol+=dp[0b1111111111][N][i]
print(sol % 1000000000)

