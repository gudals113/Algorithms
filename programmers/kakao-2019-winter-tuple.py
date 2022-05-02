def solution(s):
    answer = []
    
    s=s[1:-1]
    L = []
    
    open=0
    made = ''
    tmp=[]
    print(s)
    for i in range(len(s)):
        if s[i]=='{':
            open=1
            continue
        
        elif s[i] == '}':
            open=0
            tmp.append(int(made))
            made=''
            
            L.append(tmp)
            tmp=[]
            continue
        
        if open==0:
            continue
        
        elif s[i]==',':
            tmp.append(int(made))
            made=''   
        
        else:
            made+=s[i]
            
    L.sort(key=len)
    answer.append(L[0][0])
    for i in range(1,len(L)):
        num = set(L[i]) - set(L[i-1])
        
        answer.append(list(num)[0])
            
    print(answer)
    return answer

solution("{{1,2,3},{2,1},{1,2,4,3},{2}}") 
solution("{{20,111},{111}}")

