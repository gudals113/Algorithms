#두용액 two pointer
N = int(input())
A= list(map(int,input().split()))
A.sort()

tmp=float('inf')
sol=[]
s,e = 0, N-1

while s!=e:
    if tmp >= abs(A[s]+A[e]):        
        tmp=abs(A[s]+A[e])
        sol= [ A[s],A[e] ]
        if tmp==0:
            break
    if A[s]+A[e]==0:
        sol=[A[s], A[e]]
     
    if A[s]+A[e] <0:        
        s+=1
        
    elif A[s]+A[e]>0:
        e-=1
    
print(*sol)