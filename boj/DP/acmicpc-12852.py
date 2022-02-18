# 1로 만들기 2
from collections import deque
N = int(input())
maxCost = 10**6
dp = [ [maxCost,0] for _ in range(N+1)] # idx = idx 값을 가지는 숫자 ,dp[idx]= [최솟값, 이전 숫자]
dp[1] = [0,0]
q=deque([1])

while q :
    e = q.popleft() 
    if e==N:
        break
    
    count = dp[e][0] 
    
    result1 = e*3        
    result2 = e*2
    result3 = e+1
    
    if result1<=N and dp[result1][0] == maxCost:
        q.append(result1)
        dp[result1][0] = count+1
        dp[result1][1] = e 
    
    if result2<=N and dp[result2][0] == maxCost:
        q.append(result2)
        dp[result2][0] = count+1
        dp[result2][1] = e 
    
    if result3<=N and dp[result3][0] == maxCost:
        q.append(result3)
        dp[result3][0] = count+1
        dp[result3][1] = e 
          

sol = dp[N][0]
print(sol)
target=N
for i in range (sol+1) :
    print(target,end=' ')
    target = dp[target][1]    

