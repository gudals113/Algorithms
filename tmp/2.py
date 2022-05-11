from collections import defaultdict

def solution(call):
    call
    answer = ''
    dict = defaultdict(int)
    place = defaultdict(list)
    for i in range(len(call)):
        for j in range(i,len(call)):
            word = call[i:j+1]
            
            dict[word] +=1
            place[word].append([i,j])

    tmp = 0
    sol = []
    for key in dict:
        
        if dict[key]>tmp :
            tmp = dict[key]
            sol=[key]
        
        elif dict[key]==tmp:
            sol.append(key)
            # if len(sol[0]) == len(key):
            #     sol.append(key)
            # elif len(sol[0]) <len(key) or :
            #     sol = [key]

    
    visited=[0 for _ in range(len(call))]
    for i in range(len(sol)):
        word = sol[i]
        PL = place[word]
        
        for j in range(len(PL)):
            s,e = PL[j]
            if visited[s]==0:
                for idx in range(s,e+1):
                    visited[idx]=1
   
   
    for i in range(len(call)):
        if visited[i]==0:
            answer+=call[i]
            
        
    print(answer)
        
solution('abcabcdefabc')