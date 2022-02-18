#문자열 폭발
def check(i):
    if len(stack) < len(bomb) : #여기서 틀렸넹
        return False
    
    for idx in range(len(bomb)):
        if bomb[len(bomb)-1 -idx ] != stack[-1-idx]:
            return False
    return True

line = list(input())
bomb = input()
stack=[]
i=0

while True:
    if i == len(line):
        break
    
    stack.append(line[i])
    
    if line[i] == bomb[-1]:
        if check(i)==True:
            for _ in range(len(bomb)):
                stack.pop()
    i+=1 

if len(stack)==0:
    print('FRULA')    
else:
    print(''.join(stack))

#문자열 list로 변환하면 왜 공백 포함되는거지
#''.join(list) 잘 이용하자 - >시간복잡도는 몇이지 for 으로 한글자씩 end='' 하면 o(n)