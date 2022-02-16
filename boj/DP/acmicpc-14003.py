#가장 긴 증가하는 부분 수열 5
#루프 실행마다 실제 lis를 구하는 것이 아니라 lis보다 긴 수열이 증가해야지 dp가 완전히 갱신된다.

#반례
# 10
# 3 8 10 1 5 7 9 8 9 6

# 10
# 3 8 10 1 5 7 9 6 10

N= int(input())
arr = list(map(int, input().split()))

dp=[[0,0]] # index도 저장
tracking=[0 for _ in range(N+1)]
idx=0

for i in range(len(arr)):
    
    target = arr[i]
    if len(dp)==1 or dp[-1][0] < target :

        tracking[i] = dp[-1][1]
        dp.append([target,i])
        idx = i
        
        
    else:
        s,t = 0, len(dp)
        
        while t-s>1:
            
            mid = (s+t)//2      
            if dp[mid][0] >= target :
                ans = mid
                t=mid
            else:
                s=mid
    
        dp[ans][0]=target
        dp[ans][1]=i
        tracking[i] = dp[ans-1][1]
        

sol=[]
for _ in range(len(dp)-1):
    sol.append(arr[idx])
    idx = tracking[idx] 
sol.reverse()
print(len(dp)-1)
print(*sol)
