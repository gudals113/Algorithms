from collections import defaultdict
from email.policy import default


def solution(rooms, target):
    answer = []
    nameDict=defaultdict(list)
    roomDict=defaultdict(list)
    
    for str in rooms:
        rst = str.split(']')
        roomnum = int(rst[0][1:])
        nameList = rst[1].split(',')
        for name in nameList :
            roomDict[roomnum].append(name)
            nameDict[name].append(roomnum)
            
    candidate=[]
    for name in nameDict:
        if name in roomDict[target]:
            continue
        
        have = len(nameDict[name])
        tmp = float('inf')
        for near in nameDict[name] :
            tmp = min(tmp,abs(target-near))
        
        candidate.append([have,tmp,name])
        
    candidate.sort(key=lambda x:(x[0],x[1],x[2]))
            
        
    for can in candidate:
        answer.append(can[2])
    
    return answer


solution(["[403]James", "[404]Azad,Louis,Andy", "[101]Azad,Guard"],	403)