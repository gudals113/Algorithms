def solution(expression):
    answer = 0
    orderList = [
        ['+','-','*'],
        ['+','*','-'],
        ['-','+','*'],
        ['-','*','+'],
        ['*','+','-'],
        ['*','-','+']
             ]
    
    NUM = []
    REL = []
    tmp =''
    for word in expression:
        if word == '-' or word =='+' or word == '*':
            
            NUM.append(tmp)
            REL.append(word)

            tmp =''

        else:
            tmp+=word
    NUM.append(tmp)


    for order in orderList:
        num = NUM[:]
        rel = REL[:]

        for i in range(3):
            
            idx = 0
            while idx < len(rel):
      
                if rel[idx]==order[i] :
                    
                    val = eval(num[idx] + rel[idx] + num[idx+1])
                    del num[idx]
                    del num[idx]
                    num.insert(idx,str(val))
                    del rel[idx]
                    
                    
                else:
                    idx+=1
                
        
        tmp = int(num[0])

        answer = max(abs(tmp), answer)
    print(answer)
    return answer




solution("100-200*300-500+20")