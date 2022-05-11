from collections import defaultdict
def solution(gems):
  
    dict1=defaultdict(int)
    dict2=defaultdict(int)
    for gem in gems:
        dict1[gem]+=1
        dict2[gem]+=1
    

    s=0
    e= len(gems)-1
    while e>=s:
        sg = gems[s]
        eg = gems[e]        
        
        if dict1[eg] >1 :
            dict1[eg]-=1
            e-=1
        
        elif dict1[sg] >1:
            dict1[sg]-=1
            s+=1
        
        else:
            break
    tmp1 = [s+1, e+1]
    l1= e-s
   
 
    s=0
    e= len(gems)-1
    while e!=s:
        sg = gems[s]
        eg = gems[e]        
        
        
        if dict2[sg] > 1:
            dict2[sg]-=1
            s+=1
        
        elif dict2[eg] > 1 :
            dict2[eg]-=1
            e-=1
        
        else:
            break
    
    tmp2 = [s+1,e+1]
    l2 = e-s
    
    if l2<l1 :
        answer = tmp2
    elif l1<l2:
        answer = tmp1
    else:
        if tmp1[0] > tmp2[0]:
            answer=tmp2
        else:
            answer=tmp1
            
    print(answer)
    return answer


solution(['A','B','A','B','B','C','F','A','B','C'])

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["XYZ", "XYZ", "XYZ"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])

solution(['DIA', 'EM', 'EM', 'RUB', 'DIA'])