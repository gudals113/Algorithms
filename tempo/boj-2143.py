#부분배열의 합
T = int(input())
N = int(input())
A= [0]+list(map(int, input().split()))
M = int(input())
B = [0]+list(map(int, input().split()))

prefixA = [ 0 for _ in range(N+1)]
for i in range(1,N+1):
    prefixA[i]=prefixA[i-1]+A[i]
    
prefixB = [ 0 for _ in range(M+1)]
for i in range(1, M+1):
    prefixB[i]=prefixB[i-1]+B[i]
    
G= [[0 for _ in range(M+1)] for _ in range(N+1)]
for i in range(N+1):
    for j in range(M+1):
        G[i][j]=prefixA[i]+prefixB[j]


for i in range(1, N+1):
    for j in range(1, M+1):

        # x=1 에서 i 까지 중에서 prefixA[x] 
        # y=1 에서 j 까지 중에서 prefixB[y]