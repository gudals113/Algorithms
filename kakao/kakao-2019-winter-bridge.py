def solution(stones, k):
    answer = 0
    
    s,e = -1, max(stones)+1
    
    while s+1<e:
        
        mid = (s+e)//2
        
        
        tmp=0
        check = 0
        for i in range(len(stones)):
            if stones[i] < mid :
                tmp+=1
            else:
                tmp=0
                
            if tmp >= k :
                e = mid
                check=1
                #다돌렸는데도 안넘어가면 s =mid
                break
        
        if not check : 
            answer = mid
            s = mid
            
            
        
                
    print(answer)  
                
        
    
    
    return answer


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],	3)