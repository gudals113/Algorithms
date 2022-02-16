
def solution(S):
    
    S=list(S.split())
    length= len(S)
    stack = []
    LIMIT = 2**20
    
    for i in range(length):
        cur = S[i]
        if cur == "POP" :
            if len(stack)==0:
                return -1
            
            stack.pop()
            
        elif cur == "DUP" :
            if len(stack)==0:
                return -1
            
            e = stack.pop()
            if type(e) is not int :
                return -1
            
            stack.append(e)
            stack.append(e)
        elif cur == "+" :
            if len(stack)==1 or len(stack)==0:
                return -1
            
            a = stack.pop()
            b = stack.pop()
            if type(a) is not int or type(b) is not int :
                return -1
            
            tmp = a+b
            if tmp<0 or tmp>=LIMIT :
                return -1
            
            stack.append(tmp)
        elif cur == '-':
            if len(stack)==1 or len(stack)==0:
                return -1
            
            a= stack.pop()
            b= stack.pop()
            
            if type(a) is not int or type(b) is not int :
                return -1
            
            tmp = a-b
            if tmp<0 or tmp>=LIMIT :
                return -1
            
            stack.append(tmp)
        else:
            
            e = int(cur)
            if e<0 or e>=LIMIT :
                return -1
            stack.append(e)
    
    ans = stack.pop()
    return ans

sol = solution("1048575 DUP +")
print(sol)