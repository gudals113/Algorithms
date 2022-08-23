#회의실 배정 4
# hint 220715 poolc study
# 이분 탐색, dp, 그리디

N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))

L.sort(key=lambda x:x[1])    

dp = [ 0 for _ in range(N)]
dp[0] = L[0][2]

for i in range(N):
    s,e,p = L[i]
    if L[i-1][1] <= s :
        dp[i]=dp[i-1]+p

    
    else :
        a,b = -1, i
        target = -1
        while b-a>1:
            mid = (a+b)//2
            _,be,_ = L[mid]    
            if be <= s:
                a= mid
                target = mid
            else:
                b = mid       
                         
        dp[i] = max(dp[i-1], dp[target]+p)
            
    
print(dp[N-1])

