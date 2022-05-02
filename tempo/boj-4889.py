# ans=[]
idx = 1

while True:
    S = input()
    if S[0] == '-':
        break
    
    stack=[]
    sol = 0
    for i in range(len(S)):
        s = S[i]
        
        if stack==[]:
            if s=='}':
                sol+=1
                stack.append('{') 
            else:
                stack.append(s)
        
        elif stack[-1]=='{' and s=='}':
            stack.pop()
        
        else:
            stack.append(s)

    
    while len(stack)>0:
        a = stack.pop()
        b = stack.pop() 
        if a==b:
            sol+=1
        elif a=='>' and b=='<':
            sol+=2
        
                
    print(f'{idx}. {sol}')
    idx+=1
        
