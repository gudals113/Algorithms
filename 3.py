from collections import defaultdict

def solution(tstring, variables) :
    dict=defaultdict(str)
    loopdict = defaultdict(str)
    G = variables
    for i in range(len(G)):
        target = G[i][0]
        value = G[i][1]
        
        if value[0]!='{':
            dict[target] = value
            
    for i in range(len(G)):
        target = G[i][0]
        value = G[i][1]
        if value[0] =='{':
            inValue = value[1:-1]
            if inValue in dict : 
                dict[target]= dict[inValue]

            else:
                loopdict[target]=inValue
                
    #word 랑 DFS 도중에 있는거랑 같으면 무한루프, 다르면 그거 dict에 저장하기
    def DFS(word):
        if word in visited :
            return False
        visited[word] = 1
        
        
        value = loopdict[word]
        if value not in loopdict:
            return value
        
        rst = DFS(value)
        return rst

    
    #main : this is 처리
    #반복문 돌리며 괄호 안에 단어 dict에 있으면 그대로 넣기, 없으면 DFS 돌려서 찾기
    answer=''
    i=0
    while i <len(tstring):
        now = tstring[i]
    
        if now =='{':
            for j in range(i+1,len(tstring)):
                if tstring[j]=='}':
                    word = tstring[i+1:j]
                    i = j+1
                    
                    if word in dict:
                        answer+=dict[word]
                        
                    elif word not in loopdict:
                        answer+='{'+word+'}'
                        dict[word] = '{'+word+'}'
                    else:
                        
                        visited=defaultdict(int)
                        rst = DFS(word)
                        if rst == False: #무한루프면
                            answer += '{'+word+'}'
                            dict[word] = '{'+word+'}'
                        else: 
                            answer += '{'+rst+'}'
                            dict[word] = '{'+rst+'}'

                    break
         
        else:
            answer+=now
            i+=1    
        
    print(answer)
    return answer
    
    # rst = DFS('template')
    # print(rst)
    

    # print(dict)  
    # print(loopdict)
    


# solution('this is {template} {template} is {state}', [["template", "string"], ["state", "changed"]]) 
#"this is string string is changed"

# solution("this is {template} {template} is {state}",[["template", "string"], ["state", "{template}"]])
#"this is string string is string"

solution("this is {template} {template} is {state}" ,[["template", "{state}"], ["state", "{template}"]])
# "this is {template} {template} is {state}"

solution("this is {template} {template} is {state}", [["template", "{state}"], ["state", "{templates}"]])
# "this is {templates} {templates} is {templates}"

solution("{a} {b} {c} {d} {i}",[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]])