# 나누기 prefix Sum
N = int(input())
A = list(map(int, input().split()))

def getPrefix(A): #O(N)
    prefix = [0 for _ in range(len(A))]
    prefix[0]=A[0]
    for i in range(1,len(A)):
        prefix[i] = prefix[i-1] + A[i]    
    return prefix


prefix1 = getPrefix(A)

if prefix1[-1] % 4 != 0:
    print(0)

elif prefix1[-1]==0:
    tmp=0
    for i in range(N):
        if prefix1[i]==0:
            tmp+=1
    
    sol = (tmp-1)*(tmp-2)*(tmp-3)//6
    print(sol)
    
else:   
    div = prefix1[-1]//4
    
    dp = [ [0 for _ in range(4)] for _ in range(N) ]
    
    for i in range(1, N):
        n = prefix1[i]
        if n == div:
            dp[i][1] = dp[i-1][1]
            dp[i][2] = dp[i-1][2]
            dp[i][3] = dp[i-2][3]
            
            dp[i][0]=dp[i-1][0]+1
            
            
        elif n == div*2:
            dp[i][0] = dp[i-1][0]
            dp[i][2] = dp[i-1][2]
            dp[i][3] = dp[i-2][3]
            
            dp[i][1] = dp[i-1][1]+dp[i-1][0]
            
        elif n == div*3:
        
            dp[i][0] = dp[i-1][0]
            dp[i][1] = dp[i-1][1]
            dp[i][3] = dp[i-2][3]
            
            dp[i][2] = dp[i-1][2]+dp[i-1][1]
            
            
        # elif n == div*4:  # 이것 때문에 틀렸다! dp 최적화 하는 방법도 있을듯?
        #     dp[i][0] = dp[i-1][0]
        #     dp[i][1] = dp[i-1][1]
        #     dp[i][2] = dp[i-2][2]
            
        #     dp[i][3] = dp[i-1][3]+dp[i-1][2]
            
            
        else:
            dp[i]= dp[i-1]  
    print(dp[N-1][2])
            
            
            