def solution(queue1, queue2):
    half_len = len(queue1)
    sum_list = queue1 + queue2
    sum_all = sum(queue1) + sum(queue2)
    
    if sum_all&2 == 1:
        return -1
    
    half_all = sum_all // 2
    
    sum_list.extend(sum_list)
    
    candidate = []
    e = 0
    tmp = 0
    
    for s in range(len(sum_list)-1) :
        while tmp < half_all and e < len(sum_list)-1 :
            tmp += sum_list[e]
            e+=1    
        if tmp == half_all and e-s <len(sum_list)-1 :
            candidate.append([s,e])
            
        tmp -= sum_list[s]
    
    
    if len(candidate)==0 :
        return -1
    
  
    answer = len(sum_list)
    for s,e in candidate :
        
        if s >= half_len*2 :
            break
        
        tmp = 0
        if s < len(queue1) :
            tmp+=s

            if e > len(queue1) :
                tmp+=  (e - len(queue1))
             
            elif e== len(queue1) :
                pass

            else : 
                #정답까지 전부 옮기고, 정답 빼고 다 옮겨와
                tmp+= e-s 

                tmp+=len(queue2) + s
                
                
                
                #근데 s가 처음이면 어떡해?####
        
    

        elif s>=len(queue1):
            tmp += ( s- len(queue1))
            
            if e > len(queue1) + len(queue2) :
                tmp += (e - len(queue1) - len(queue2))
            
            elif e == len(queue1) + len(queue2) :
                pass
            else:
                tmp += e-s
                tmp += len(queue1) + s
    
     
        
        answer = min(answer,tmp)

    return answer


# rst = solution([3, 2, 7, 2]	,[4, 6, 5, 1])
rst1= solution([1, 2, 1, 2],	[1, 10, 1, 2])
# rst2= solution([1, 1]	,[1, 5])

# print(rst,rst1,rst2)