# 히스토그램
# stack
# 220904
N =int(input())
answer = 0
stack = [[0,-1]]
for i in range(1,N+1):
    h = int(input())
    
    if stack[-1][1] <= h:
        stack.append([i,h])
        
    else:
        while True:
            if stack[-1][1] < h :
                stack.append([ bi  ,h])
                break
            
            bi, bh = stack.pop()            
            answer = max(answer, bh*(i - (bi) ) )

while stack :
    bi,bh = stack.pop()
    answer = max(answer, bh*(N+1-bi))

print(answer)