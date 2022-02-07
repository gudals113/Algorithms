#스티커 (DP)
T=int(input())

for _ in range(T):
    N= int(input())
    arr0=list(map(int, input().split()))
    arr1=list(map(int, input().split()))

    dp=[ [0,0] for _ in range(N)]


    for i in range(N):
        if i==0:
            dp[0][0]= arr0[0]
            dp[0][1]= arr1[0]

        elif i==1:
            dp[1][0]= dp[0][1]+arr0[1]
            dp[1][1]= dp[0][0]+arr1[1]

        elif i>=2:
            dp[i][0]= max(dp[i-2][1], dp[i-1][1]) + arr0[i]
            dp[i][1]= max(dp[i-2][0], dp[i-1][0]) + arr1[i]

    # print(dp)
    print(max(dp[N-1][0], dp[N-1][1]))
