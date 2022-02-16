#알고리즘분석 수업 과제
global A,B
A=list(map(int, input().split()))
B=list(map(int, input().split()))
#A[0] >= B[0], A[N] <=B[N]

def crossingPoint(s,t):
    if (t-s<=1) and (A[s]>=B[s]) and (A[t]<=B[t]):
        return s
    
    m= (s+t)//2
    if (A[m] == B[m]) and (A[m+1]<=B[m+1] ):
        return m

    if (A[s] > B[s]) and (A[m] > B[m]):
        return crossingPoint(m,t)
    elif (A[s] > B[s]) and (A[m] < B[m]):
        return crossingPoint(s,m)

sol=crossingPoint(0,len(A)-1)
print(sol+1)