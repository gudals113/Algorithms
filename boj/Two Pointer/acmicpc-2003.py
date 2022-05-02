# 투포인터

# N, M = map(int,input().split())
# arr= list(map(int, input().split()))

# sol,s,e,tmp =0, 0, 0, 0
# while True:
    
    
#     if tmp>=M:
#         tmp-=arr[s]
#         s+=1
    
#     elif e==N : # e==N이어도 tmp >=M이면 종료 하면 안된다
#         break
    
#     elif tmp<M:
#         tmp+=arr[e]
#         e+=1
        
#     if tmp==M:
#         sol+=1
        
# print(sol)

N,M = map(int,input().split())
A = list(map(int, input().split()))
sol,tmp=0,0
s,e,=0,0

while s!=N:
    
    if tmp>=M or e==N:
        tmp-=A[s]
        s+=1
    else:
        tmp+=A[e]
        e+=1
    
    if tmp==M:
        sol+=1
        
print(sol)