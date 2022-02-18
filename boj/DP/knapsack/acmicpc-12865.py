#평범한 배낭
N, K = map(int, input().split())
diamond =[ [0,0] ] #W,V
for _ in range(N):
    diamond.append(list( map(int, input().split()) ) )
    
dp = [ 0 for _ in range(K+1)] 
for i in range(1,N+1):
    cost, benefit = diamond[i][0], diamond[i][1]
    for j in range(K, 0, -1) :
        if j-cost>=0 :
    
            dp[j] = max(dp[j], dp[j-cost] + benefit )    
        
print(dp[K])

#개수 무제한이면 이렇게 해도 되나?
# N, K = map(int, input().split())
# diamond =[ [0,0] ] #W,V
# for _ in range(N):
#     diamond.append(list( map(int, input().split()) ) )
    
# dp = [ 0 for _ in range(K+1)] 
# for i in range(1,N+1):
#     cost, benefit = diamond[i][0], diamond[i][1]
#     for j in range(1, K+1) :
#         if j-cost>=0 :
    
#             dp[j] = max(dp[j], dp[j-cost] + benefit )    
        
# print(dp[K])
