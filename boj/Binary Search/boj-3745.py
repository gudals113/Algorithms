# 오름세
# sol 220804 14:54-
# 이분 탐색

import sys
input = sys.stdin.readline
while True:
    N = input()
    if not N:
        break
    N = int(N)
    L = list(map(int, input().split()))
    dp = []
    
    for i in range(N):
        if len(dp)==0 or dp[-1] < L[i]:
            dp.append(L[i])
        
        else:
            s,e = -1, len(dp)
            target = 0
            while e-s>1:
                mid = (s+e)//2
                if dp[mid] >= L[i]:
                    target = mid
                    e=mid
                    
                else:
                    s = mid

            dp[target] = L[i]
    
    print(len(dp))