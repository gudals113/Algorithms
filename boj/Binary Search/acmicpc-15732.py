# 도토리 숨기기 (binary search) 1300번문제와 유사
import sys
def input():
    return sys.stdin.readline()

N,K,D = map(int, input().split())
rule=[]
for i in range(K):
        line = list(map(int, input().split()))
        rule.append(line)

ans=0
s,t=0, N+1
while t-s>1:
    
    mid = (s+t)//2
    
    tmp=0
    for i in range(K):
        r = rule[i]
        A,B,C = r[0], r[1], r[2]
        
        if mid < A  : 
            continue
        
        if mid > B :
            dtr = ( (B-A)//C) +1
            
        else:
            dtr = ( ( mid-A )//C ) +1
        tmp+=dtr
    

        
    if tmp >= D:
        ans = mid
        s,t=s,mid
    
    elif tmp < D:
        s,t = mid,t
        
print(ans)
    
        