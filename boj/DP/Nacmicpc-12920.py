#평범한 배낭2
from math import log2
N, M = map(int, input().split()) #물건 개수, 가방 용량
stuff = [[0,0,0]]  #무게, 가치, 개수

#N 갱신해주어서 풀어야한다. 15 = 1+2+4+8
for _ in range(N) :
    line = list(map(int, input().split()))
    num = line[2]
    binaryNum = bin(num)
    print(binaryNum)
    



dp = [ 0 for _ in range(M+1)] #dp[j] 용량 j일 때 최대 가치

for i in range(1, N+1):
    cost, value, num = stuff[i][0], stuff[i][1], stuff[i][2]
    
    for j in range(M,cost-1,-1):
        dp[j] = max(dp[j], dp[j-cost]+value)

print(dp[M])