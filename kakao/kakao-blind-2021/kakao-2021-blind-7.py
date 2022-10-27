INF = float('inf')
def solution(sales, links):
    answer = 0
    N = len(sales)
    sales = [0]+sales
    
    tree = [[] for _ in range(N+1)]
    for u,v in links:
        tree[u].append(v)
        tree[v].append(u)
    
    dp = [[INF, INF ] for _ in range(N+1) ]
    
    visited = [0 for _ in range(N+1)]
    def DFS(node):
        
        visited[node]=1
        
        minVal = 0
        l = []
        
        isLeaf=True
        for next in tree[node]:
            if not visited[next]:
                isLeaf = False
                sel,nosel = DFS(next)
                l.append([next,sel,nosel, abs(sel-nosel)])
                minVal += min(sel,nosel)

        if isLeaf:
            dp[node][0] = sales[node] # 내가 선택된 경우
            dp[node][1] = 0           # 내가 선택되지 않은 경우
            return dp[node][0], dp[node][1]
        
        #l에서 적어도 하나는 sell.
        l.sort(key=lambda x:x[3])
        tmp=0

        check = 0
        for i in range(len(l)):
            csel, cnosel = l[i][1], l[i][2]
            if csel<=cnosel : 
                check=1
            tmp+=min(csel,cnosel)
        if not check:
            tmp= tmp- l[0][2] + l[0][1]

        dp[node][0] = sales[node]+ minVal
        dp[node][1] = tmp
        return dp[node][0], dp[node][1]
    
    a,b = DFS(1)
    answer = min(a,b)
    print(answer)
    return answer

solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])
solution([5, 6, 5, 3, 4],[[2,3], [1,4], [2,5], [1,2]])