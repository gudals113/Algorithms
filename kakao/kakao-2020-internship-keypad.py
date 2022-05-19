def solution(numbers, hand):
    answer = ''
    LN = [3,0]
    RN = [3,2]
    dict ={ 1:[0,0], 2:[0,1], 3:[0,2],
            4:[1,0], 5:[1,1], 6:[1,2],
            7:[2,0], 8:[2,1], 9:[2,2],
            0:[3,1]
           }
    
    for n in numbers:
        x,y = dict[n]
        if y==1:
            LD = abs(LN[0] - x ) + abs(LN[1]-y)
            RD = abs(RN[0] - x ) + abs(RN[1]-y)
            if LD > RD :
                answer+='R'
                RN = [x,y]
            elif LD <RD :
                answer+='L'
                LN = [x,y]
                
            else:
                if hand == 'left':
                    answer+='L'
                    LN = [x,y]
                else:
                    answer+='R'
                    RN = [x,y]
                    
            
        elif y==0:
            answer+='L'
            LN = [x,y]
            
        elif y==2:
            answer+='R'
            RN = [x,y]
        
    
    
    return answer
    
    
    
    
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right")