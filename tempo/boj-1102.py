#발전소, 비트마스킹, dp, 220509sol

G = []
#입력값 받기
N = int(input())
for _ in range(N):
    G.append(list(map(int, input().split())))
status = input()
P = int(input())

#상태 비트로 표현하기
firstStat = 0

count = 0
#YNN이면 001
for i in range(N):
    if status[i]=='Y' :
        firstStat |= 1<<(i) 
        count+=1
        
toSet = P-count
if toSet <=0 :
    print(0)
    quit()
elif count == 0:
    print(-1)
    quit()

dp = [ [ -1 for _ in range(2**N) ] for _ in range(toSet+1)]
dp[0][firstStat] = 0

for bitStat in range(firstStat, 2**N):
    
    for p in range(1,toSet+1):    
        
        if dp[p-1][bitStat] != -1:
            
            for idx in range(N) :
                if bitStat & 1<<idx == 1<<idx : 
                    
                    
                    for next in range(N):
                        if next!=idx and bitStat & 1<<next != 1<<next:
                        # if next!=idx:
                            
                            newStat = bitStat | 1<<next
                            cost = G[idx][next]
                            
                            if dp[p][newStat] == -1 :
                                dp[p][newStat] = dp[p-1][bitStat] + cost    
                            else:
                                dp[p][newStat] = min( dp[p][newStat], dp[p-1][bitStat] + cost   )

answer = float('inf')  
for i in range(2**N):
    if dp[toSet][i] != -1:
        answer=min(dp[toSet][i] , answer)
print(answer)

