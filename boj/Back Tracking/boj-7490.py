#0 만들기 (backtracking)
def checkZero(L):
    
    str = ''.join(L).replace(' ', '')
    isZero = eval(str)
    if isZero==0 :
        return True
    
    
def makeZero(num):    
        if num == N :
            if checkZero(visited):
                print(''.join(visited))
            
            return True
        
        visited.append(' ' + str(num+1))
        makeZero(num+1)
        visited.pop()
        
        
        visited.append('+' + str(num+1))
        makeZero(num+1)
        visited.pop()
        
        visited.append('-' + str(num+1))
        makeZero(num+1)
        visited.pop()
        
        
        
T= int(input())
for _ in range(T):
    sol=0
    N = int(input())
    visited =['1']
    makeZero(1)
    
    print()