#좋은 수열 backtracking, sol 220527
N = int(input())

def check(s):
    
    idx=2
    while idx*2 <= len(s):
        if s[-1*idx:]==s[-2*idx:-1*idx]:
            return False
        idx+=1
    return True
        
    

def DFS(num ,last):
    if not check(num) :
        return False
    
    if len(num) == N:
        print(num)
        return True
        
    
    for next in range(1,4):
        if next!=last :
            if DFS(num+str(next),next):
                return True
    return False

DFS('1', 1)

