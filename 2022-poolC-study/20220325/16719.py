from collections import deque


S = input()
alphabet = [ deque([]) for _ in range(26)]

for i in range(len(S)):
    num = ord(S[i])-65
    alphabet[num].append(i)

str=''
idx=-1
while True:
    
    for i in range(27):
        if i == 26:
            idx=0
            break
        
        
        if len(alphabet[i])>0 and alphabet[i][0] > idx :
            idx = alphabet[i].popleft()
            str+=S[idx]
            print(str)
            break

    if len(str)==len(S):
        break
