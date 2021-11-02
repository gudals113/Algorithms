#백준 1918번 후위 표기 (stack)

prefix = input()
stack = []
postfix = ''

for word in prefix:

    if 65 <= ord(word) <= 90:
        postfix += word

    elif word == '(':
        stack.append(word)

    elif word == ')':

        while True:
            
            if stack[-1] == '(':
                stack.pop()
                break
            else:
                postfix += stack.pop()

    elif word == '+' or word=='-':
        
        while True:
            if stack == []:
                break
            elif stack[-1]=='(':
                break
            else:
                postfix += stack.pop()

        stack.append(word)

    elif word == '*' or word== '/':
        
        while True:
            
            if stack == []:
                break
            
            elif stack[-1] == '+' or stack[-1] == '-' or stack[-1] =='(':
                break

            else:
                postfix += stack.pop()

        stack.append(word)
        
    # print(stack,"stack")
    
for _ in range( len(stack) ):
    postfix += stack.pop()


print(postfix)
