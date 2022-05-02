T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

prefixA = [0 for _ in range(N+1)]
prefixA[0]=0
prefixB = [0 for _ in range(M+1)]
prefixB[0]=0

for i in range(1, N+1):
    prefixA[i] = prefixA[i-1]+A[i-1]
    
for i in range(1,M+1):
    prefixB[i] = prefixB[i-1]+ B[i-1]

# prefixA[i] = A[0]+ A[1] + ...A[i-1]
print(prefixA)
for i in range(1,N+1):
    for j in range(0,i):
        tmp = prefixA[i] - prefixA[j]
        
        
        
        print(tmp)