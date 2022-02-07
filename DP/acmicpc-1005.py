#Acm craft (dp)
T=int(input())
def craft(last) :
    if dp[last] !=-1:
        return dp[last]
    
    cndt = path[last]
    if cndt==[] :
        return time[last] 
    
    tmp=0
    for e in cndt :
        tmp = max(craft(e), tmp)
    
    dp[last]=tmp+time[last]
    return dp[last]


for _ in range(T):
    
    N, K = map(int, input().split() )
    
    time = [0] + list(map(int, input().split()))
    path = [ [] for _ in range(N+1) ]
    dp=[ -1 for _ in range(N+1)]
    
    for i in range(K):
        u,v = map(int, input().split())
        path[v].append(u) # 역순으로 저장, 임의의 건물을 건설하기 위해 필요한 조건을 찾을 수 있도록    
    des= int(input())
    sol=craft(des)
    print(sol)

#dp = 0으로 초기화 하면 안된다 건물 짓는 시간이 0일수도 있다!! 주의!!