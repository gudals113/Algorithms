# 카드 구매하기 (dp)
N= int(input())
arr = [0] + list(map(int,input().split()))

dp=[0 for i in range(N+1)]


for i in range(1,N+1):    
    tmp=arr[i]
    for j in range(1,i):
        tmp = max(tmp, dp[i-j] + arr[j] ) 
    dp[i] = tmp
print(dp[-1])