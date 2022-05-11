from collections import defaultdict, deque
from shutil import move


def solution(n, k, cmd):
    
    
    #한 번이라도 삭제 되었다면 체크
    answer = ['O' for _ in range(n)]
    
    #현재 삭제 여부 확인
    # dict = defaultdict(int)
    # for i in range(n):
    #     dict[i] = 1
    
    #현재 삭제 된 것들 저장
    stack = []
    dlt = defaultdict(int)
    
    
    # 길이를 그냥 게속 N 이라고 생각하고 , idx를 속임수 쓰는거지
    last = n-1
    idx = k
    for c in cmd :
        
        if len(c) == 3:
            moveWay = c[0]
            moveNum = c[2]
            
            #여기서 순서대로 나와야 하네!
            if moveWay == 'D' :
                moveNum = int(moveNum)
                
                for num in dlt :
                    if idx < num <= idx + moveNum :
                        moveNum+=1     
                        
                idx += moveNum    

            elif moveWay == 'U' :
                moveNum = int(moveNum)
                
                for num in dlt:
                    if  idx- moveNum <= num < idx :
                        moveNum +=1
                
                idx -= moveNum
                
        elif c == 'C' :
            if idx == last :
    
                for i in range(idx-1,-1,-1):
                    if i not in dlt:              
                        stack.append(idx)
                        dlt[idx] = 1
                        last = i
                        idx = i
                        break
                    

                    
            else:
                stack.append(idx)
                dlt[idx] = 1
                
                for i in range(idx,n):
                    if i not in dlt:
                        idx=i
                        break
    
    
        elif c == 'Z' :
            i = stack.pop()
            del dlt[i]
            if i >last :
                last = i
        
        
        print(c, idx, dlt)
            
    for num in dlt :
        answer[num] = 'X'        
    
    sol = ''.join(answer)
    
    return sol

# rst = solution(8,	2	,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
rst = solution(8,	2	,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
print(rst)