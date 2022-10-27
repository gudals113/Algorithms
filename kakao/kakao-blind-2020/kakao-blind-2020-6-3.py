# kakao-blind-2020-6-3.py
from itertools import permutations


def solution(n, weak, dist):
    answer = -1
    m = len(weak)
    for i in range(m):
        weak.append(weak[i]+n)
    
    dist.sort(reverse=True)

    def find():
        for num in range(1, len(dist)+1):
            #친구 1명 배치 - 모든 친구 배치하는 경우 순서
            p = list( permutations( [i for i in range(num)] ,num ) )
            # 순서에 있는 학생들을 차례대로 배치한다.
            for order in p:
                
                for idx in range(0,m):
                    
                    fixed = {}
                    for friend in order :
                        
                        if idx >= len(weak):
                            break

                        start = weak[idx]
                        end = start + dist[friend]
                        
                        while idx<len(weak):
                            point = weak[idx]
                            if start<=point<=end:
                                if point>n :
                                    point = point%n
                                fixed[point] = 1
                            else:
                                break
                            idx +=1
                        
                    if len(fixed)==m:
                        return num
            
        return -1
    
    answer = find()

    return answer


solution(12	, [1, 5, 6, 10]	,[1, 2, 3, 4])
# solution(12,	[1, 3, 4, 9, 10],	[3, 5, 7])