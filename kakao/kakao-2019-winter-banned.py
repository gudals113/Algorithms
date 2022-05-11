#2019 카카오 개발자 겨울 인텁십 - 불량 사용자

def combination(candidate) :
    
    visit=[]
    for i in range( len (candidate)) :
        if len(visit)==0:
            for user in candidate[i] :
                visit.append([user])
                
        else :
            newVisit=[]
            for tmp in visit :
                for user in candidate[i]:
                    if user not in tmp :
                        newVisit.append(tmp + [user])
            visit = newVisit[:]
    
    newArr=[]
    for item in visit :
        setted = set(item)
        if setted not in newArr:
            
            newArr.append(setted)
    
    return len(newArr)
           
def solution(user_id, banned_id):
    ban_len , user_len= len(banned_id) , len(user_id)
    
    candidate= [ [] for _ in range(ban_len)]
    for i in range(ban_len):
        each_ban = banned_id[i]

        visited = [1 for _ in range(user_len)]
        for j in range(user_len):
            each_user = user_id[j]
            
            if len(each_ban) != len(each_user) :
                visited[j] =0
                
            else :
                for idx in range(len(each_ban)) :
                    if each_ban[idx] =='*' or each_ban[idx] == each_user[idx] :
                        pass
                    else :
                        visited[j]=0
                        break
        
        for k in range(user_len):
            if visited[k]==1:   
                candidate[i].append(k)  
    
            
    answer = combination(candidate)
    return answer

   
                
            
                    
sol = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(sol)