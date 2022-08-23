# boj-2568.py 전기줄-2, n lon n lis, sol220629
N = int(input())
dict={}
for i in range(N):
    a,b = map(int,input().split())
    dict[b]=a    
dict = sorted(dict.items(), key=lambda item:item[1])

dp = []
P = []
for i in range(N):
    val = dict[i][0]
    if len(dp)==0 or (len(dp)>0 and dp[-1]<val):
        dp.append(val)
        P.append(len(dp)-1)

    else:
        s,e = -1, len(dp)
        target=0
        while e-s>1:
            mid = (s+e)//2
            
            if dp[mid] >= val:
                e=mid
                target=mid
                
            elif dp[mid]<val:
                s=mid
        
        dp[target]=val
        P.append(target)

idx = len(dp)-1
sol =[]

for i in range(N-1,-1,-1):
    
    if P[i]==idx :
        idx-=1

    else:
        sol.append(dict[i][1])
        
    
sol.sort()
print(N-len(dp))
for i in range(len(sol)):
    print(sol[i])