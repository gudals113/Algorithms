#카카오 2021 블라인드 - 메뉴 리뉴얼

#비트로 표현하기
def changeToNum(arr) :
    
    newArr =[]
    
    for i in range(len(arr)) : # 모든 코스에 대하여 실행
        course = arr[i]
        
        bit = 0
        for j in range(len(course)):
            num = ord(course[j]) -65
            
            bit |= 1<<num
            
        newArr.append(bit)        
    return newArr


#변환된 orders를 서로 비교하며 and해서 저장하면 된다. # 비교하지말고 course 원소 개로 이뤄진 코스 탐색?
# 저장된 것들 중에서 2번 이상 등장하는 것들만 모아
# 2번 이상 등장하는 것들 중에서 1의 개수가 course에 담긴 원소만큼 있는 것들만 남겨
# acde가 두 번 이상 등장 ? acd 가능 근데 예를들어 xyz가 3번 등장하면 이걸 return

def solution(orders, course): 
    orders = changeToNum(orders)
    
    
    
    
    
    answer = []
    return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])