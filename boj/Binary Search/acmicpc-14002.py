# 가장 긴 증가하는 부분 수열 4
# O(n**2) 로 풀기
N= int(input())
arr = [0]+list(map(int, input().split()))

dp=[ [0,0] for _ in range(N+1)]
ans = [0,0]
for i in range(1,N+1):
    
    tmp=0
    for j in range(1,i) :   # 현재 원소 기준 이전 모두 탐색
        if arr[i] > arr[j] : # 현재 원소보다 작은 원소(index = j) 발견 시 
            
            if dp[j][0] >= tmp : # j일 때 가장 긴 증가 수열의 길이 
                tmp = dp[j][0]
                dp[i][1] = j  # 현재 원소 이전 모두 탐색하며 긴 증가 수열 길이 갱신되면 인덱스 j 저장 
                
    dp[i][0] = tmp+1       #dp 갱신
    
    if ans[0] <= dp[i][0]: #현재 dp가 최대 길이라면 ans에 길이와 수열의 마지막 인덱스 저장 
        ans[0]=dp[i][0]
        ans[1]=i


idx=ans[1]
sol=[]

for i in range(ans[0]) : # ans[1]에 저장된 마지막 인덱스부터 역추적
    sol.append(arr[idx])
    idx = dp[idx][1]
    
print(ans[0])
for i in range(ans[0]-1,-1,-1):
    print(sol[i],end=' ')