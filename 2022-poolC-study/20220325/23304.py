#아카라카 팰린드롬
S = input()

def check(S):
    #짝수
    # print(S)
    
    if len(S)<=1:
        return True
    if len(S)%2==0:
        
        front = S[:len(S)//2]
        back = S[len(S)//2:][::-1]
        if front == back:
            
            tmp1 = check(front)
            tmp2 = check(back)
            
            if tmp1 and tmp2 :
                return True
        else:
            return False
    else:
        front = S[:len(S)//2]
        back = S[1+len(S)//2:][::-1]
        
        
        if front == back:
            
            tmp1 = check(front)
            tmp2 = check(back)
            
            if tmp1 and tmp2 :
                return True
        else:
            return False
    
    
result = check(S)
if result :
    print('AKARAKA')
else:
    print('IPSELENTI')
    
    
        
        


