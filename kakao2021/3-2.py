from collections import defaultdict, deque
from shutil import move


def solution(n, k, cmd):
    
    dict = defaultdict(list)
    for i in range(n):
        dict[i] = [i-1,i+1]
    dict[0] = [None,1]
    dict[n-1] = [n-2,None]
    
    answer = ['O' for _ in range(n)]
    
    stack = []
    
    idx = k
    
    for c in cmd :
        if len(c) >= 3:
            moveWay, moveNum = c.split(' ')
            moveNum = int(moveNum)
            
            
            if moveWay == 'D' :
                for _ in range(moveNum) :
                    idx = dict[idx][1]
            
            else:
               for _ in range(moveNum) :
                    idx = dict[idx][0]
                    
        elif c == "C":
            answer[idx]='X'
            prev , next = dict[idx]
            stack.append([prev,idx,next])
            
            if next ==None: #마지막이라면
                idx = prev
            else:
                idx = next
            
            if prev == None :
                dict[next][0] = None #None                
            elif next == None:
                dict[prev][1] = None #None
            else : 
                dict[prev][1] = next
                dict[next][0] = prev

        elif c=='Z' :
            pi,i,ni =  stack.pop()
            answer[i] = 'O'
            
            if pi == None:
                dict[ni][0] = i
            
            elif ni == None :
                dict[pi][1] = i
                
            else:
                dict[pi][1] = i
                dict[ni][0] = i
                  
    return ''.join(answer)

# rst = solution(8,	2	,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
rst = solution(8,	2	,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(rst)