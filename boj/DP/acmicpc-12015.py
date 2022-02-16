#가장 긴 증가하는 부분 수열 2
#3(12738번)도 동일한 방법
#루프 실행마다 실제 lis를 구하는 것이 아니라 lis보다 긴 수열이 증가해야지 dp가 완전히 갱신된다.
N= int(input())
arr = list(map(int, input().split()))

dp=[]

for i in range(len(arr)):
    
    target = arr[i]
    if dp==[] or dp[-1] < target :
        dp.append(target)
        
    #target보다 큰 수 중 최소값 위치 찾기
    else:
        s,t = -1, len(dp)
        
        while t-s>1:
            
            mid = (s+t)//2      
            if dp[mid] >= target :
                ans = mid
                t=mid
            else:
                s=mid
                
        dp[ans]=target
    # print(dp)
    
# print(len(dp))
print(*dp)