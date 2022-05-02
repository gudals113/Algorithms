#카카오 2022 blind 주차요금
from collections import defaultdict
import math


def solution(fees, records):
    answer = []
    dict = {}
    soldict=defaultdict(int)
    
    for i in range(len(records)):
        info = records[i].split(' ')
        time = info[0].split(':')
        h,m = map(int,time)
        car = info[1]
        io = info[2]
        
        if io == 'IN':
            dict[car]=[h,m]
            
        else :
            inH, inM = dict[car]
            if m < inM:
                h-=1
                m+=60
                
            tmp = (h-inH)*60 + m-inM
            soldict[car]+=tmp
            del(dict[car])
    
    keyL = list(dict.keys())
    for car in keyL:
        h,m = 23,59
        inH, inM = dict[car]                      
        tmp = (h-inH)*60 + m-inM
        soldict[car]+=tmp
        
    
    
    solL = list(soldict.keys())
    solL.sort()
    dT = fees[0]
    dF = fees[1]
    dt = fees[2]
    df = fees[3]
    
    for car in solL:
        time = soldict[car]
        tmp=dF
        if time > dT : 
            time = time - dT
            d = time / dt 
            d = math.ceil(d)
            tmp += d*df
        answer.append(tmp)
    
    
    
    return answer

rts = solution([180, 5000, 10, 600], ["05:34 5961 IN", 
                                "06:00 0000 IN", 
                                "06:34 0000 OUT", 
                                "07:59 5961 OUT", 
                                "07:59 0148 IN",
                                "18:59 0000 IN",
                                "19:09 0148 OUT",
                                "22:59 5961 IN",
                                "23:00 5961 OUT"])
print(rts)