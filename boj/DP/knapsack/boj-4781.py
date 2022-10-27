# 사탕 가게
# sol 220915
# 1차원 knapsack
from collections import defaultdict


while True:
    N, M = input().split()
    if N=='0': break
    N =int(N)
    M = int(0.05+float(M)*100)
    dp = [0 for _ in range(M+1)]
    
    for i in range(1,N+1):
        c, p = input().split()
        c = int(c)
        p  = int(0.05+float(p)*100.00)    
        
        for m in range(p,M+1):
            dp[m] = max(dp[m], dp[m-p]+c)

    print(max(dp))