# LCS 3
# sol 220902
# dp

A,B,C = ' '+input(),' '+input(),' '+input()

dp = [ [ [ '' for _ in range(1+len(C)) ] for _ in range(1+len(B)) ] for _ in range(1+len(A)) ]
answer = ''
for i in range(1,len(A)):
    for j in range(1,len(B)):
        for k in range(1,len(C)):
            if A[i]==B[j] and B[j]==C[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + A[i]
                
                if len(answer) < len(dp[i][j][k]):
                    answer = dp[i][j][k]
                
            else:
                a,b,c = len(dp[i][j][k-1]), len(dp[i][j-1][k]), len(dp[i-1][j][k])
                t = max(a,b,c)
                if a==t:
                    target = dp[i][j][k-1]
                elif b==t:
                    target = dp[i][j-1][k]
                else:
                    target = dp[i-1][j][k]

                dp[i][j][k] = target


# print(answer)
print(len(answer))