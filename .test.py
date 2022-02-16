# #평범한 배낭2
# N, M = map(int, input().split())
# stuff = [[0,0,0]]
# # costSum = 0
# for _ in range(N) :
#     line = list(map(int, input().split()))
#     # costSum += line[0] * line[2]
#     stuff.append(line)
    
# # stuff[]  = 무게, 만족도, 개수
# dp=[ [0 for _ in range(M+1)] for _ in range(N+1) ]

# # 모든 물품에 대하여 루프
# for i in range(1, N+1):
#     cost = stuff[i][0]
#     bnf = stuff[i][1]
#     num = stuff[i][2]
#     idx = num
    
#     #최대무게 부터 무게1까지 에 대하여 루프 
#     for j in range(M,0,-1) :
        
#         dp[i][j] = dp[i-1][j]
        
#         if j>=cost*idx:
#             # 여기서 모든 인덱스 봐야겠다? 
#             dp[i][j] = max(dp[i][j], dp[i-1][j-cost*idx]+bnf*idx)

            
#         elif 0<=j<cost*idx and idx>1:
#             idx-=1
#             if j>=cost*idx:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j-cost*idx]+bnf*idx)  
#         print(i,j,dp[i][j])       
    
# print(dp[N][M])


s = '012345'

print(s[1:])


print(s[1:3])#차이 크기만큼 리턴
print(s[3:1:-1])