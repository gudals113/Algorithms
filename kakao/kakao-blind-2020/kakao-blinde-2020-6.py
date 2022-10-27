
from collections import deque


def solution(n, weak, dist):
    answer = -1
    dist.sort(key=lambda x:-x )
    M = len(weak)
    copyed = weak[:]
    for i in range(len(copyed)):
        weak.append(copyed[i]+n)
    
    
    def check(num):
        notWork = {}
        for i in range(M):
            notWork[weak[i]] = 1
        
        # 1번 친구 어디에 배치, 2번 친구 어디에 배치 차례대로 탐색.
        for friend in range(num):
            d = dist[friend]
            sorted_notWork = sorted(notWork.items())
            
            candidate = []
            lastCovered = 0
            
            #freind를 배치할 시작 지점을 갱신하며, count 최대 & 가장 먼 두 지점 커버하는 곳 찾기
            for start,_ in sorted_notWork:
                tmp = 0 
                end = start+d
                
                for point,_ in sorted_notWork:    
                    if start<=point<= end : 
                        tmp +=1
                        lastCovered = point
                    elif point < start and point <= end%n and end>n :
                        tmp +=1
                        lastCovered = point + n
                         
                        
                candidate.append([tmp, lastCovered-start, start ])
            candidate.sort(key = lambda x:(x[0],-x[1]))
            select = candidate[0][2]
            
            #select point 부터 d 만큼 처리
            rng = select + d
            for point,_ in sorted_notWork:
                if start<=point<=rng:
                    del notWork[point]
                elif point< start and point<= rng%n:
                    del notWork[point]
            print(friend,'번 친구는 여기서 시작',select, candidate)        
        print(num, notWork)
        if len(notWork)==0:
            return True
        
    s,e = -1, len(dist)+1
    while e-s>1:
        mid = (s+e)//2
        covered = 0
        
        if check(mid):
            covered=1
        
        if covered==1:
            e= mid
            answer = mid
        else:
            s = mid  
    
    print('answer',answer)
    return answer

solution(12	,[1, 5, 6, 10]	,[1, 2, 3, 4])
# solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7])