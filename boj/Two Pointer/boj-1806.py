N, S =map(int, input().split() )
A = list(map(int,input().split()))

s,e=0,0
sol = 100001
tmp = 0
while s<N:
    if sol ==1:
        break
    
    if tmp >=S or e==N:
        tmp-=A[s]
        s+=1
    
    else :
        tmp+=A[e]
        e+=1
    
    if tmp >=S:
        sol = min(sol, e-s)


if sol==100001:
    print(0)
else:
    print(sol)