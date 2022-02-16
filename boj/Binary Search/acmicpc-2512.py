#예산 , binary search, 
#상한액 기준 이분탐색
N=int(input())
ask = list(map(int, input().split()))
M = int(input())

s, t = -1, M+1
while s+1<t:
    # print(s,t)
    mid = (s+t) //2
    
    tmp=0
    for i in range(N):
        tmp+= min(mid, ask[i])
    
    if tmp <=M :
        ans = mid
        s= mid
    else :
        t = mid
        
if ans == M :
    print(max(ask))
else:
    print(ans)