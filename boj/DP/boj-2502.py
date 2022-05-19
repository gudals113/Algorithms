#떡 먹는 호랑이 (dp) sol220513
D, K = map(int,input().split())

dp=[ [0,0] for _ in range(D+1)]
dp[0] = [1,0]
dp[1] = [0,1]

for i in range(2,D):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
    
a,b= dp[D-1]
f, s = 0,0
for i in range(1,100001):
    if (K - a*i ) % b == 0:
        f = i
        s = (K - a*i ) // b
        break
    
if f>=s:
    print(s)
    print(f)
    
else:
    print(f)
    print(s)
    