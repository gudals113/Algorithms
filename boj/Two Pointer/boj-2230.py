#수 고르기 투포인터
N,M = map(int,input().split())
L = []
for _ in range(N):
    L.append(int(input()))

L.sort()

s,e=0,0
sol= float('inf')
tmp = M

while s<N:
    tmp = L[e]-L[s]
    
    if tmp >= M:
        sol = min(sol, tmp)
      
    if tmp == M:
        break  
    
    elif e==N-1 or tmp > M :
        s+=1
    
    elif tmp < M:      
        e +=1

print(sol)
        
        