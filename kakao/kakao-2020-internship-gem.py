from collections import defaultdict
def solution(gems):
    answer=[]
    checkDict= {}
    
    for gem in gems:
        if gem not in checkDict:
            checkDict[gem]=1
            
    gemLen = len(checkDict)

    dict=defaultdict(int)
    
    s,e=0,0 #s포함, e포함
    dict[gems[s]]=1
    tmp=len(gems)+1
    answer=[1,1]
    
    while s<=e:
        # print(s,e)
        
        if e==len(gems)-1 or len(dict) == gemLen :
            dict[gems[s]]-=1
            if dict[gems[s]] == 0:
                del dict[gems[s]]
            s+=1
            
        else:
            e+=1
            dict[gems[e]]+=1
            
        if len(dict) == gemLen :
            if tmp>e-s+1 :
                tmp = e-s+1
                answer = [s+1,e+1]


    return answer


# solution(['HI','HELLO'])
# solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
# solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
# solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])

# solution(['DIA', 'EM', 'EM', 'RUB', 'DIA'])
