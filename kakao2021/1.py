def solution(s):
    answer = 0
    dict = {
        'one' : 1,
        'two' : 2,
        'three' :3,
        'four' : 4,
        'five' :5,
        'six' : 6,
        'seven' :7,
        'eight' : 8,
        'nine' :9,
        'zero' :0
        }
    
    
    sol=[]
    tmp =''
    for word in s:
     
        if tmp in dict :
            sol.append(dict[tmp])
            tmp=''


        if  48<=ord(word) <=57 :
            sol.append(int(word))
                        
        else:
            tmp+=word
        
    if tmp!='':
        sol.append(dict[tmp])
        
    
    for i in range(len(sol)-1, -1,-1):
        answer += (10**i)*sol[len(sol)-1-i]
    print(answer)
    
    
    return answer

solution("one4seveneight")
solution('o')

