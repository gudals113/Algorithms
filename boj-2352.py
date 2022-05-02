N= int(input())
L = list(map(int, input().split()))

dp=[]
for i in range(N):
    if len(dp)==0 :
        dp.append(L[i])
        
    elif dp[-1] < L[i]:
        dp.append(L[i])
        
    else:
        
        s,e = -1, len(dp)
        tmp=0
        while e-s>1:
            mid = (s+e)//2
            
            if dp[mid]>L[i]:
                tmp = mid
                s,e = s,mid
            else :
                s,e = mid, e
                
        dp[tmp] = L[i]

# print(dp)
print(len(dp))