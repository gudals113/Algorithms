from collections import deque

def solution(atmos):
    answer = 0
    used=0

    for i in range(len(atmos)):
        day = atmos[i]
        li = day[0]
        veli = day[1]
        
        if  li>=81 or veli>=36 :
            if used==0 :
                answer+=1
                used+=1
                
            elif used==1:
                used+=1
            
            elif used==2:
                used=0
                
            if li>=151 and veli >=76:
                used=0
        
        else :
            if used==1:
                used+=1
            elif used==2:
                used=0
            
            

    return answer
