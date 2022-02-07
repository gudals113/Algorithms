#미제출
#답지 참고
N=int(input())
k=int(input())
ans=0
s,t= 0, (N**2)+1

while s+1<t : 
    m=(s+t)//2
    count=0
    for i in range(1,N+1):
        count += min(m//i, N)
    
   
    
    if k>count : 
        s,t = m,t
    elif k<=count :
        ans=m
        s,t = s,m
        
print(ans)    
