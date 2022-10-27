# kakao-blind-2019-3.py
# 다중 딕셔너리로 풀어버리기. 이런 비슷한 문제 있었던 것 같은데 기억이 안나네
from itertools import combinations


def solution(relation):
    answer = 0
    #총 학생 수
    N = len(relation)
    
    #총 속성 수
    M = len(relation[0])
   
    materials = [i for i in range(M)]

    def check(c):


        for l in range(1,len(c)+1):
            for answerSet in answerList[l]:
                
                if set(answerSet) & set(c) == set(answerSet):
                    
                    return False
        return True    

    # 최소성을 유지하기 위해 키의 개수를 1개에서부터 늘려가며 시행한다.
    answerList = [[]for _ in range(len(materials)+1)]
    for num in range(1,len(materials)+1):

        # 최소성 유지를 위해 재료에서 삭제한다.
        comb = list(combinations( materials, num))

        for c in comb:
            
            longDict = {}
            #유일성 체크
            isPossible = True
            for student_idx in range(N):
                rel = relation[student_idx]
                
                #포인터 역할을 하는 nowDict
                nowDict = longDict
                for atb in c:
                    atbName = rel[atb]
                    if atbName not in nowDict:
                        nowDict[atbName] = {}
                    
                    nowDict =  nowDict[atbName]

                if len(nowDict)==0:
                    nowDict[student_idx]=1

                else:
                    isPossible = False
                    break
                    
            if isPossible :
                if check(c):
                    answerList[len(c)].append(c)
                    answer+=1

    return answer

solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
solution( [["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"] ])