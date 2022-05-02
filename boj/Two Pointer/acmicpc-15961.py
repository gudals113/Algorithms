#회전 초밥 # 슬라이딩 윈도우
from collections import defaultdict
N, d, k , c = map(int, input().split())
A=[ int(input()) for _ in range(N)]
A.extend(A)
D=defaultdict(int)

D[c]+=1

s,e=0,0
sol=1
while e<k:
    D[A[e]]+=1
    e+=1
while e<len(A):
    sol = max(sol, len(D))
    
    D[A[s]]-=1
    if D[A[s]]==0:
        del D[A[s]]
    D[A[e]]+=1
    s+=1
    e+=1
    
print(sol)
    
    
    
    