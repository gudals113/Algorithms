from collections import defaultdict

def solution(rooms, target):
    answer = []
    nameDict=defaultdict(list)
    roomDict=defaultdict(list)
    blackDict =defaultdict(int)
    
    for str in rooms:
        rst = str.split(']')
        roomnum = int(rst[0][1:])
        nameList = rst[1].split(',')
        
        if roomnum== target:
            for name in nameList:
                blackDict[name] = 1
                if name in nameDict:
                    del(nameDict[name])
        
        else:
            for name in nameList :
                if name not in blackDict:   
                    roomDict[roomnum].append(name)
                    nameDict[name].append(roomnum)
            
    candidate=[]
    for name in nameDict:
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
solution(["[101]Azad,Guard", "[202]Guard", "[303]Guard,Dzaz"],202)