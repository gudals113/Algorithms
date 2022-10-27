# kakao-blind-2020-6-2.py
from copy import deepcopy

def solution(n, weak, dist):
    answer = -1
    dist.sort(key=lambda x:-x )
    M = len(weak)
    copyed = weak[:]
    for i in range(len(copyed)):
        weak.append(copyed[i]+n)
    
    def check(friend,num,fixed):
        
        if friend == num :
            if len(fixed) == M:
                return True
            return False
        
        d = dist[friend]
        for start in range(M):
            
            newFixed = []    
            end = weak[start]+d
            idx = start
            
            while idx<len(weak):
                point = weak[idx]
                if point > end:
                    break
                
                if point > n :
                    point = point%n
                
                if point not in fixed:
                    newFixed.append(point)
                    
                idx+=1
            
            # if point in fixed:
                # continue
            
            for p in newFixed:
                fixed[p]=1
            if check(friend+1, num, fixed):
                return True
            for p in newFixed:
                del fixed[p]
            
        return False
            
    s,e = -1, len(dist)+1
    while e-s>1:
        mid = (s+e)//2
        
        covered = 0
        if check(0,mid,{}):
            covered=1
        
        if covered==1:
            e= mid
            answer = mid
        else:
            s = mid  
    

    return answer

solution(12	,[1, 5, 6, 10]	,[1, 2, 3, 4])
solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7])