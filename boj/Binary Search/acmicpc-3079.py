#입국심사, binary search
#총 소요 기준 이분탐색
N,M = map(int, input().split())

immi=[]
for _ in range(N):
    immi.append(int(input()))

s=-1
t=10**18 +1
ans=0

while s+1<t:
    print(s,t)
    mid = (s+t) //2
    acm=0
    for i in range(N):
        acm+= mid//immi[i]

    if acm>=M:
        ans = mid
        t=mid
    else:
        s=mid
        
print(ans)



