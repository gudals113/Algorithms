#Maximum Subarray 구간합, dp 
def kadaneSolution():
    N = int(input())
    A = list(map(int,input().split()))
    
   
    for i in range(1, N):
        A[i]=max(A[i], A[i-1]+A[i])
        
    print(max(A))

def getMinSolution():
    N = int(input())
    A = list(map(int, input().split()))
    prefix = [0 for _ in range(N)]
    prefix[0]=A[0]
    for i in range(1,N):
        prefix[i]=prefix[i-1]+A[i]

    # 0 to i 구간에서 최대 prefix => max(prefix[i] - prefix[k]) = prefix[i] - min(prefix[k])
    minPrefix = 0
    sol=float('-inf')
    for i in range(N):
        tmp = prefix[i] - minPrefix
        sol = max(tmp, sol)
        minPrefix = min(minPrefix, prefix[i])
        
    print(sol)
        
T = int(input())
for _ in range(T):
    # kadaneSolution()
    getMinSolution()
    

