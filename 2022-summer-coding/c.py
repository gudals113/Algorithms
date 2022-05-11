from collections import defaultdict
def solution(line):
    answer = []
    left = [1,0]
    right = [1,9]
    
    dict = defaultdict(list)
    dict['0'] = [0,9]
    for i in range(1,10):
        strI = str(i)
        dict[strI]=[0,i-1]
    qwert = 'QWERTYUIOP'
    for i in range(10):
        dict[qwert[i]] = [1,i]    
    
    for word in line:
        targetX,targetY = dict[word]
        sideDistL = abs(left[1]-targetY)
        sideDistR = abs(right[1]-targetY)
        distL = abs(left[0]-targetX) + sideDistL
        distR = abs(right[0]-targetX) + sideDistR
        
        if distL < distR :
            left=dict[word]
            answer.append(0)
        elif distL > distR:
            right = dict[word]
            answer.append(1)
            
        else :
            if sideDistL < sideDistR :
                left = dict[word]
                answer.append(0)
                
            elif sideDistL > sideDistR :
                right = dict[word]
                answer.append(1)
                
            else:
                if targetY <=4 :
                    left = dict[word]
                    answer.append(0)
                    
                else:
                    right = dict[word] 
                    answer.append(1)

    
    
    return answer

solution('QWER')