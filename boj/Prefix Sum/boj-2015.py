#수들의 합4
# prefix SUm
from collections import defaultdict


N, K = map(int, input().split())
L = list(map(int, input().split()))
S = [0]
for i in range(N):
    S.append(S[-1]+L[i])

answer = 0
idx_dict = defaultdict(list)
for i in range(N,0,-1):
    SUM = S[i]
    
    if SUM == K :
        answer+=1
    

    target = SUM+K
    answer += len(idx_dict[target])
    
    idx_dict[SUM].append(i)
    
print(answer)