#양팔 저울
N=int(input())
weight = list(map(int, input().split()))
T= int(input())
question = list(map(int, input().split()))
dp= [ [-1,-1] for _ in range(40001)]

for i in range(N):
    now = weight[i]
    
    for j in range(1,15000): #같은 추 중복 사용하게 되는거 어떻게 해결하지 i를 표시해서 현재 추에서 바뀐거면 불가능하도록
        
        if dp[j][0]==1 and dp[j][1]!=i:
            
            new_add=now+j
            new_sub=abs(j-now)
            
            if dp[new_add][0] !=1:
                dp[new_add][0] =1
                dp[new_add][1] =i
            
            if dp[new_sub][0]!=1:
                dp[new_sub][0]=1
                dp[new_sub][1]=i
                
    if dp[now][0] !=1:    
        dp[now][0] = 1
        dp[now][1] = i

sol=[]
for q in (question):
    if dp[q][0]==1:
        sol.append('Y')
    else:
        sol.append('N')
print(*sol)