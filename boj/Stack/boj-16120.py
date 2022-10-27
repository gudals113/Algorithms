# PPAP
# sol 220902
# string, stack

S = input()

stack = []
i = 0
while i <len(S):
    s = S[i]

    if s == 'P':
        if len(stack)>=3 and stack[-1]=='A' and stack[-2]=='P' and stack[-3]=='P':
            stack.pop()
            stack.pop()
            stack.pop()
            
        stack.append(s)

    elif s == 'A':
        if len(stack)>=2 and stack[-1] =='P' and stack[-2] == 'P':
            stack.append(s)            
        else:
            stack = ['NP']
            break
    i+=1
    
if stack ==['P']:
    print('PPAP')
else:
    print('NP')

