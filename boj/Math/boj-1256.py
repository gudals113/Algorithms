# boj-1256.py
# 사전
# 조합
N , M , K = map(int, input().split())
def cal_comb(a,b):
    if a>=b:
        n = a
        m = b
        
    else:
        n = b
        m = a
        
    tmp = 1
    
    for d in range(n+m, n,-1):
        tmp*=d

    for d in range(1,m+1) :
        tmp=tmp//d

    return tmp

rst = cal_comb(N,M)

if rst < K :
    print(-1)
    
else:
    count = 0
    visited=[]

    while True :
        if N<=0 or M<=0:
            break
        startA = cal_comb(N-1,M)
        # startZ = cal_comb(N,M-1)
        
        if count+startA < K:
            count+=startA
            visited.append('z')
            M-=1
        
        elif count+startA >= K:
            visited.append('a')
            N-=1
            
    if N>0:
        for _ in range(N):
            visited.append('a')
    if M>0:
        for _ in range(M):
            visited.append('z')
            
    answer = "".join(visited)
    
    print(answer)
             

    