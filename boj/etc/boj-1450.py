# # 냅색문제
# hint 220808
# 알고리즘 분류 힌트
# meet in the middle
from collections import defaultdict

N,C = map(int, input().split())
L = list(map(int,input().split()))
leftN = N//2 
rightN = N - leftN

leftL = L[:leftN]
rightL = L[leftN:]

def getS(L):
    S = defaultdict(int)
    for i in range(len(L)):
        candidate = defaultdict(int)
        num = L[i]    
        candidate[num]=1
        
        #잠시 저장
        for past in S :
            candidate[num+past] += S[past]
        #딕셔너리 갱신
        for c in candidate:
            S[c]+=candidate[c]
    
    return sorted(S.items())

leftS = [(0,1)]+getS(leftL)
rightS = [(0,1)]+getS(rightL)

suffixRightS = [rightS[0][1]]
for i in range(1,len(rightS)):
    suffixRightS.append( suffixRightS[-1] + rightS[i][1] )

answer = 0
for i in range(len(leftS)):
    s,e=-1,len(rightS)
    target = -1
    while e-s>1:
        mid = (s+e)//2
        
        if rightS[mid][0] + leftS[i][0] <= C :
            s = mid
            target = mid
        else:
            e = mid
            
    if target!=-1:    
        answer += leftS[i][1] * suffixRightS[target]

print(answer)