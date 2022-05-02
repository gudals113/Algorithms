#세용액 two pointer
N= int(input())
A=list(map(int, input().split()))
A.sort()

tmp=float('inf')
sol=[]
for i in range(N-2):
    fix = A[i]    
    s,e = i+1, N-1
    while s!=e:
        if abs(A[s]+A[e]+fix) < tmp:
            tmp = abs(A[s]+A[e]+fix)
            sol = [ fix, A[s], A[e] ]
        
        if A[s]+A[e]+fix == 0 :
            break
          
        elif A[s]+A[e]+fix < 0 :
            s+=1
            
        else:
            e-=1

print(*sol)