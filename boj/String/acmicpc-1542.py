#잃어버린 괄호
string = input()
stack=[]
newArr=[]

# input 받아서 기호는 그대로 숫자는 변환해서 저장 -> 더하기부터 계산 -> 빼기 계산
def changing() :
    global stack, newArr    
    t,num=1, 0
    while(stack):
        num += int(stack.pop()) * t
        t*=10
    newArr.append(num)
    

for i in range(len(string)):
    if string[i] == '-' or string[i]=='+':
        changing()
        newArr.append(string[i])
    else:
        stack.append(string[i])
changing()

i=0
while True:
    if i >= len(newArr):
        break
    
    if newArr[i] !='+':
        stack.append(newArr[i])

    else:
        i+=1    
        a=stack.pop()
        b=newArr[i]
        stack.append(a+b)
        
    i+=1    

sol=stack[0]
for i in range(2, len(stack), 2):
    sol -= stack[i]

print(sol)

# 이렇게 하지 않고 - 기준으로 그냥 input 받는 방법이 있다.
# input().split('-')