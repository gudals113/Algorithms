# kakao-blind-2019-1.py

from collections import defaultdict
from email.policy import default


def solution(N, stages):
    answer = []
    ingDict = defaultdict(int)
    for userStage in stages:
        ingDict[userStage]+=1
    
    #기본값은 0    
    faultRate=[]
    
    faultUnder = [0 for _ in range(N+2)]    
    faultUnder[N+1] = ingDict[N+1]
    for stage in range(N,0,-1):
        faultUnder[stage] = ingDict[stage] + faultUnder[stage+1]

    for stage in range(1,N+1) :
        if faultUnder[stage]==0: tmp = 0
        else: tmp = ingDict[stage]/faultUnder[stage]
        faultRate.append([stage,tmp])
    
    faultRate.sort(key=lambda x:(-x[1],x[0]))
    
    print(faultRate)
    print(faultUnder)
    
    for stage,tmp in faultRate:
        answer.append(stage)
    return answer

solution(5,	[2, 1, 2, 6, 2, 4, 3, 3])