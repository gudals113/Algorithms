# boj-2616.py
# 소형기관차
# dp
# sol220801 
N = int(input())
L = list( map( int, input().split()) )
K = int(input())

prefix = [L[0] for _ in range(N)]

for i in range(1,N):
    prefix[i] = prefix[i-1] + L[i]

# dp[i][j] = i번째 기차까지 j개 선택시 최대
dp= [ [0 for _ in range(4)] for _ in range(N)]

dp[K-1][1] = prefix[K-1]

# 마지막 기차의 인덱스가 i, 총 K칸 운반가능 일 떄, 승객 수 : prefix[i] - prefix[i-K]

for i in range(K,N):
    dp[i][1] = max(dp[i-1][1], prefix[i]-prefix[i-K])
    
    if i>=2*K-1:
        dp[i][2] = max(dp[i-1][2], prefix[i]-prefix[i-K] + dp[i-K][1])
    
    if i>=3*K-1:
        dp[i][3] = max(dp[i-1][3], prefix[i]-prefix[i-K] +  dp[i-K][2])
        
print(dp[N-1][3])

