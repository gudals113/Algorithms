#회문 string
def second(str,left,right):
    count=0
    while left<right:
        if str[left]!=str[right]:
            count+=1
        left+=1
        right-=1
    return count


T = int(input())
for _ in range(T):
    str=input()
    sol=0
    if str==str[::-1]:
        print(sol)
    else:
        left,right =0, len(str)-1
        while left<right:
            if str[left]!=str[right]:
                
                tmp1=second(str, left+1,right)
                tmp2=second(str, left, right-1)
                if tmp1 == 0 or tmp2==0 :
                    sol=1
                else:
                    sol=2
                        
                break
            left+=1
            right-=1
            
            
        print(sol)
    
