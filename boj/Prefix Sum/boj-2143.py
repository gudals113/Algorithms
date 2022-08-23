#2143번 두 배열의 합
# prefix sum
# sol 220718
from collections import defaultdict


T = int(input())
N = int(input())
A = [-1]+list(map(int, input().split()))
M = int(input())
B = [-1]+list(map(int, input().split()))


prefixA = [0 for _ in range(N+1)]
prefixB = [0 for _ in range(M+1)]

for i in range(1, N+1):

    prefixA[i] = prefixA[i-1]+A[i]

    
for i in range(1, M+1):
    prefixB[i] = prefixB[i-1]+ B[i]

sumDict = defaultdict(int)

# O(1,000,000)
for i in range(1,N+1):
    for j in range(0,i):
        val = prefixA[i]-prefixA[j]
        sumDict[val]+=1
        
answer = 0
for i in range(1,M+1):
    for j in range(0,i):
        val = prefixB[i]-prefixB[j]
        if (T-val) in sumDict :

            answer += sumDict[T-val]
         
            
print(answer)