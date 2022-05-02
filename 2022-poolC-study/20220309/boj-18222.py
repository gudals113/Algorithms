# X=0
# X`=1
# X= X+X` 01
# X` = 10
# 01 10 10 01 

# 1->2->4->8->16


k = int(input())
A = [0,0,1]
R= [1,1,0]



def divide(num,count):
    # 제일 가까운 2의 제곱수 찾기
    if num<=2:
        if count%2==0:
            print(A[num])
        else:
            print(R[num])
        return
    
    idx=0
    while True:
        if num<=2**idx:
            break        
        else:
            idx+=1    

    distance = 2**idx - num
    
    target = 2**(idx-1) - distance
    
    divide(target,count+1)
    
divide(k,0  )