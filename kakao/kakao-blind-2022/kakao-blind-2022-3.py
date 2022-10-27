from collections import defaultdict
from math import ceil


def solution(fees, records):
    answer = []
    
    def calculate(time):
        tmp = 0
        tmp = fees[1]
        if time>fees[0]:
            time = time - fees[0]            
            tmp += ceil(time/fees[2]) * fees[3]

        return tmp
                
        
    answerDict = defaultdict(int)
    timeDict = defaultdict(int)
    carLog = {}
    
    for record in records:
        T, C, IO = record.split()
        H,M = T.split(':')
        time = int(H)*60 + int(M)
        
        if IO=='IN':
            carLog[C] = time

        else:
            inTime = carLog[C] 
            timeDict[C] += time - inTime
            del carLog[C]    
            
    for car,inTime in carLog.items():
        time = 23*60 + 59
        timeDict[car]+= time-inTime
    
    
    for car,time in timeDict.items():
        rst = calculate(time)
        answerDict[car] = rst
   
   
   
    answerList = list(answerDict.items())
    answerList.sort(key=lambda x:x[0])
    for a in range(len(answerList)):
        answer.append(answerList[a][1])
    
    return answer

solution([180, 5000, 10, 600]	,["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])