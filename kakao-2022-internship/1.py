from collections import defaultdict


def solution(survey, choices):
    answer = ''
    
    dict = defaultdict(int)
    def select(q, score) :
        
        if score <4:
            selected =q[0]
        else:
            selected =q[1]
            
        if score==1 or score ==7 :
            dict[selected] +=3
        
        elif score == 2 or score==6 :
            dict[selected] +=2
            
        elif score==3 or score==5:
            dict[selected] +=1
            
    
    for i in range(len(survey)):
        select(survey[i], choices[i])
            
    
    if dict['R'] >= dict['T'] :
        answer+='R'
    
    else:
        answer+='T'
        
    if dict['C'] >= dict['F'] :
        answer+='C'
        
    else:
        answer+='F'
        
    if dict['J'] >= dict['M'] :
        answer+='J'
        
    else:
        answer+='M'
        
    if dict['A'] >= dict['N'] :
    
        answer+='A'
        
    else:
        answer+='N'
            
        
        
        
        
    
    return answer


solution(["AN", "CF", "MJ", "RT", "NA"]	,[5, 3, 2, 7, 5]	)