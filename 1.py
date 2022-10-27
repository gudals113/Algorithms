def solution(registered_list, new_id):
    answer = ''
    regi_dict = {}
    for id in registered_list:
        regi_dict[id]=1
    
    
    while True:
        if new_id not in regi_dict:
            answer = new_id
            break
        
        S=''
        N=''
        for i in range(len(new_id)+1):
            if i == len(new_id):
                S=new_id
                N='0'
                break

            if 48<=ord(new_id[i])<=57:
                S=new_id[:i]
                N=new_id[i:]
                break
        
        new_id = S+ str(int(N)+1)        
        
    return answer


