def solution(path):
    answer=[]
    def check(s,e):
        dL = ['N','E','S','W']
        si = dL.index(s)
        ei = dL.index(e)
        
        if ei-si == 1 or ei -si ==-3:
            return 'right'
        else:
            return 'left'
        
    L = len(path)
    nowIdx = 0
    # time = 0
    nowDir = path[nowIdx]
    
    while nowIdx  <L:
        alert = 0
    
        for i in range(nowIdx, nowIdx+6):
            if i >=L:
                
                break
            
            if path[i] != nowDir :
                turnTo = check(nowDir, path[i])
                nowDir = path[i]
                answer.append( [nowIdx, (i-nowIdx)*100, turnTo])
                
                nowIdx = i
                alert = 1
                break
            
        if alert == 0 :
            nowIdx +=1
            
    print(answer)
    return answer

solution('EEES')
solution('ESEN')
solution('EEESEEEEEENNNN')