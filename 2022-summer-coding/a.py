from collections import deque
def solution(atmos):
    answer = 0
    used=0
    
    for i in range(len(atmos)):
        day = atmos[i]
        li = day[0]
        veli = day[1]

        if li>=151 and veli >=76:
            if used==0:
                answer+=1
            elif used==1 or used==2:
                used=0
        
        elif  li>=81 or veli>=36 :
            if used==0 :
                answer+=1
                used+=1
                
            elif used==1:
                used+=1
            
            elif used==2:
                used=0
        
        else :
            if used==1:
                used+=1
            elif used==2:
                used=0
            
            
    print(answer)
    return answer


solution([[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]])