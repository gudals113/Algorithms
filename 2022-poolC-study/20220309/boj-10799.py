stack=[]
str = input()

pipe = 0
sol=0
for i in range(len(str)):
    if str[i] =='(':
        
        if str[i+1] ==')': # 레이저인 경우
            stack.append(2) # 레이저 넣어버려
        else:
            stack.append(1)
            pipe+=1
    
    else :
        tmp = stack.pop()
        if tmp==2:# 레이저인 경우
            sol+=pipe
            
        else:
            pipe-=1
            sol+=1
print(sol)