# boj-13397.py
# 파라메트릭 서치
# 이분 탐색
# 220913 sol
N, M = map(int, input().split())
L = list(map(int, input().split()))
s = -1
e = (sum(L) - min(L)) +1

#구간의 점수의 최댓값이 S가 되도록한다.
def check(s):
    count = 1
    tmpDif = 0
    tmpMax = L[0]
    tmpMin = L[0]
    dif = 0

    for i in range(1,N):

        tmpMax = max(tmpMax,L[i])
        tmpMin = min(tmpMin,L[i])
        
        if tmpMax-tmpMin > s:
            tmpMax = L[i]
            tmpMin = L[i]
            tmpDif = max(tmpDif, dif)
            count+=1
        
        else:
            dif = tmpMax - tmpMin
        
        if count > M :
            return -1
    
    tmpDif = max(tmpDif, dif)
    return tmpDif

answer = -1
while e-s>1:
    mid = (s+e)//2
    
    rst = check(mid)

    if rst!=-1:
        
        e = mid
        answer = rst
        
    else:
        s = mid
        
print(answer)