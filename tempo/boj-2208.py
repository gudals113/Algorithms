#보석 줍기dp
N,M = map(int, input().split())
A = [ int(input()) for _ in range(N)]
prefix = [0 for _ in range(N)]
prefix[0]=A[0]
for i in range(1, N):
    prefix[i] = prefix[i-1]+A[i] 

# def dynamic() :
#     dp= [[0,0] for _ in range(N)]  #현재 선택X / 선택 
#     dp[M-1][1] = prefix[M-1]

#     for i in range(M,N):
        
#         tmp1= dp[i-1][0] #이전에서도 보석 안주웠을 때
#         tmp2= dp[i-1][1] #이전 보석 주웠을 때
        
#         tmp3 = tmp2 + A[i] #이전 보석 주운거에 현재거 까지
#         tmp4 = prefix[i] - prefix[i-M] #현재 기준으로 딱 M 개 주웠을 때
        
#         dp[i][0] = max(tmp1, tmp2)
#         dp[i][1] = max(tmp3, tmp4)

#     print(max(dp[N-1]))

def getMinPrefix() :    
    
    minPrefix=min(prefix[0], 0)
    sol=max(prefix[M-1] , 0)

    for i in range(M,N):    
        sol = max(sol, prefix[i]-minPrefix)
        minPrefix= min(minPrefix, prefix[i-M])
        
    print(sol)    

# dynamic()
getMinPrefix()