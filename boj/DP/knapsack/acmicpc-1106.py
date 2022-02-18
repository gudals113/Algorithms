#호텔
# 2차원 배열로 풀기
# C, N = map(int, input().split())
# hotel=[[0,0]] #cost, benefit, Benefit per Cost

# maxCost = float('INF')

# for i in range(N):
#     line= list(map(int, input().split()))
#     hotel.append(line)

# dp = [ [ maxCost for _ in range(C+1)] for _ in range(N+1) ]
# for i in range(1,N+1):
#     benefit = hotel[i][1]
#     cost = hotel[i][0]
    
#     for j in range(1, C+1):
        
#         dp[i][j] = dp[i-1][j]
        
#         k=0
#         while True:
#             if j-(k*benefit) <=0 :
#                 dp[i][j] = min(dp[i][j], k*cost)
#                 break
            
#             else:
#                 dp[i][j] = min(dp[i][j], dp[i-1][j-k*benefit] + k*cost)
#             k+=1
           
# print(dp[N][-1])

#1차원 배열로 풀기
C, N = map(int, input().split()) # C - 적어도 얻고자 하는 이득 이 때 최소 비용 구하기
hotel=[[0,0]] #cost, benefit
for i in range(N):
    line= list(map(int, input().split()))
    hotel.append(line)

maxCost = float('INF')
dp= [maxCost for _ in range(C+100)] #dp[k] = k명 데리고 올 때 최소값 그로므로 
dp[0]=0

for i in range(1, N+1):
    cost = hotel[i][0]
    benefit = hotel[i][1]
    
    for j in range(benefit, C+100):    
        dp[j] = min(dp[j], dp[j-benefit]+cost)
        
# print(dp)     
print(min(dp[C:]))
