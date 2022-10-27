# kakao-blind-2020-2.py

# 재귀로 풀기
def solution(p):
    answer = ''
    #0 opne, 1 close
    L = []
    for i in range(len(p)):
        if p[i]=='(' : L.append('(')
        else: L.append(')')
    
    #처음에 올바른인지 체크하고 바로 리턴?
    
    #재귀 함수
    def recur(l):
        print(l)
        u = []
        v = []
        
        open ,close = 0,0
        stack = []
        for i in range(len(l)):
            if l[i] == '(' : 
                open+=1
                u.append('(')
                
                stack.append(0)

            else : 
                close += 1
                u.append(')')

                if len(stack) > 0 and stack[-1] == 0:
                    stack.pop()
                else:
                    stack.append(1)
                    
            if open > 0 and open==close:
                v = l[i+1:]
                break
        
        
        if len(v) !=0:
            right = recur(v)
        else:
            right = []
        right = ''.join(right)
        
        
        #u가 올바른 문자열이면 오른쪽만 재귀
        if len(stack) == 0:
            rst = ''.join(u) + right
            return rst
        
        #u가 올바른 문자열이 아니므로
        if len(u) > 2:
            u = u[1:-1]
        else:
            u = []
        rst = '(' + right + ')'
            
        for i in range(len(u)):
            if u[i] == '(' :
                rst+=')'
            else:
                rst+='('
            
        return rst
    
    answer = recur(L)     
    print(answer)
    return answer

solution(')(')