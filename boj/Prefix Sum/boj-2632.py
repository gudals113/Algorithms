# 피자판매
# sol 220915
# prefix sum

SIZE = int(input())
M,N = map(int, input().split())
ML,NL = [],[]
for p in range(M):
    ML.append(int(input()))
for p in range(N):
    NL.append(int(input()))
    
MDP,NDP = [0 for _ in range(SIZE+1)],[0 for _ in range(SIZE+1)]

MDP[0],NDP[0]=1,1
MSUM,NSUM = sum(ML),sum(NL)
if MSUM<=SIZE:
    MDP[MSUM]=1
if NSUM<=SIZE:
    NDP[NSUM]=1

ML = ML+ML
NL = NL+NL
for s in range(M):
    tmp = 0 
    
    for e in range(s,s+M-1):
        tmp+=ML[e]
        
        if tmp>SIZE:
            break
        
        MDP[tmp]+=1
    
for s in range(N):
    tmp = 0
    for e in range(s,s+N-1):
        tmp+=NL[e]
        
        if tmp>SIZE:
            break
        
        NDP[tmp]+=1

answer = 0
for i in range(SIZE+1):
    a,b = MDP[i], NDP[SIZE-i]
    answer += a*b
    
print(answer)
    