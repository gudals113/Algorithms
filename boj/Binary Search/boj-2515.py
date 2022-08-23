# 전시장
# sol 220804
# dp, 이분탐색
N, S = map(int, input().split())
L = [[-1,-1]]
for _ in range(N):
    L.append(list(map(int, input().split())))
L.sort(key = lambda x : x[0])
dp = [[0,0] for _ in range(N+1)]

for i in range(1,N+1):
    # 내 앞에 세울 수 있는 그림 중 최대 높이 idx 찾기
    s, e = -1, i
    target = -1
    
    while e-s>1:
        mid = (s+e)//2
        
        if L[i][0] - L[mid][0] >=S :
            target = mid
            s  = mid
            
        else:
            e = mid
            
    dp[i][0] = L[i][1]
    dp[i][1] = max(dp[i-1])

    if target!=-1:
        dp[i][0] = max(dp[target])+L[i][1]

print(max(dp[N]))
