# 파일 합치기
# dp
# sol 220810 
INF = float('inf')
T = int(input())
for _ in range(T):
    N = int(input())
    L = list(map( int, input().split()))
    
    suffix = [0]
    for i in range(N):
        suffix.append( suffix[-1]+ L [ i ])
        
    dp = [[INF for _ in range(N)]for _ in range(N)]
    
    def DFS(s,e):    
        if s==e:
            dp[s][s]=0
            return 0
        
        if dp[s][e]!= INF :
            return dp[s][e]
        
        tmp = INF
        for i in range(s, e):
            tmp1 = DFS(s,i)
            tmp2 = DFS(i+1,e)

            tmp = min(tmp, tmp1+tmp2)

        tmp += suffix[e+1]-suffix[s] 
        dp[s][e] = tmp   
        return tmp
    # answer = DFS(0,N-1)
    
    for i in range(N):
        dp[i][i] = 0
        
    for i in range(1,N):
        dp[i-1][i] = L[i-1] + L[i]

    for size in range(2,N):
        for i in range(N-size):
            j = i+size 
            tmp = INF
            for k in range(i,j):
                tmp = min(dp[i][k] + dp[k+1][j], tmp)
                
            dp[i][j] =  min(tmp + suffix[j+1]-suffix[i], dp[i][j])
            
    print(dp[0][N-1])

    