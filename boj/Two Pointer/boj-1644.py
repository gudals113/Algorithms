# 소수의 연속합
# 투 포인터
# sol 220831 
import math
N = int(input())
primeList = [True for _ in range(N+1)]

for i in range( 2, 1+ int(math.sqrt(N))):
    if primeList[i] == True:
        for j in range(2, N):
            if i*j>N :
                break
            primeList[i*j]= False

primeNum=[]
for num in range(2,N+1):
    if primeList[num] :
        primeNum.append(num)
        
s,e = -1,-1
tmp = 0
answer = 0

while True:

    if s==e and e==len(primeNum)-1 :
        break
    
    if tmp <= N and e<len(primeNum)-1:
        e+=1
        tmp+=primeNum[e]
    
    else : 
        s+=1
        tmp-=primeNum[s]
    
    if tmp == N :
        answer +=1

print(answer)