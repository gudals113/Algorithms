# kakao-2021-blind-2.py
from collections import defaultdict
from itertools import combinations

def solution(orders, course):
    answer =[]
    checkList = [defaultdict(int) for _ in range(11)]

    for order in orders :
        for num in course:
            c = list(combinations(order, num))
            for comb in c: 
                comb = list(comb)
                comb.sort()
                menu = ''.join(comb)
   
                checkList[len(menu)][menu]+=1
            
    for num in range(2,11):
        checkDict = checkList[num]
        
        if len(checkDict)==0:
            continue
        
        cl = list(checkDict.items())
        cl.sort(key=lambda x:-x[1])
        
        maxNum = cl[0][1]
        for i in range(len(cl)):
            if cl[i][1] >1 and cl[i][1]==maxNum:
                answer.append(cl[i][0])
            else:
                break
        


    answer.sort()
    print(answer)
    return answer
solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	,[2,3,4])