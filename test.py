# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    N = len(A)
    A=sorted(A)
    if A[N-1]<=0:
        return 1
    
    sol=A[0]
    for i in range(1,N):
        if A[i] >sol+1 and sol+1>0:
            return sol+1
        else:
            sol=A[i]
        
