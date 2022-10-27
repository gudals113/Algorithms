# kakao-blind-2019-5.py
def solution(food_times, k):
    answer = -1
    N = len(food_times)
    sorted_food_times=[]
    
    for i in range(N):
        sorted_food_times.append([food_times[i],i])
    sorted_food_times.sort(key=lambda x:(x[0],x[1]))
    
    deleted={}
    #남은 가짓수
    left = N
    # 지금 까지 먹은 횟수
    tmp = 0 
    # 이전 최솟값
    before = 0
    for i in range(N):
        minVal = sorted_food_times[i][0] 
        
        if tmp + left*(minVal-before) <= k:
            tmp += left*(minVal-before)
            
            deleted[ sorted_food_times[i][1] ]=1
            
            left-=1
            
            before = minVal
        
        else:
            break
    
    k = k-tmp
    

    if k<0 or left<=0 :
        return -1
    
    k = k%left
    # k번째 수 찾기 0-idx로
    now = -1
    for i in range(N):          
        if i in deleted :
            continue
        else:
            now+=1
            
        if now==k:
            answer = i+1
            break
        
    return answer

# solution([3,1,2],5)
rst = solution([10,10,5,5,10,10,5,10,10,10],60)
print(rst)