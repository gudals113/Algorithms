N=int(input())
sol=0
if N%2==1:
    print(0)
else:
    dp=[ [1 for _ in range(8)] for _ in range(N+1) ]
    for i in range(2,N+1):
        if i%2==1: #홀수 일 때
            dp[i][0b110]=dp[i-1][0b001]+dp[i-1][0b111]
            dp[i][0b011]=dp[i-1][0b100]+dp[i-1][0b111]
            dp[i][0b000]=dp[i-1][0b111]
        else:
            dp[i][0b100]=dp[i-1][0b011]
            dp[i][0b001]=dp[i-1][0b110]
            dp[i][0b111]=dp[i-1][0b000]+dp[i-1][0b110]+dp[i-1][0b011]
    print(dp[N][0b111])
