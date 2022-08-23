#트리의 지름 tree+dp, sol 220628
V = int(input())
tree=[[]for _ in range(V+1)]
dp = [[-1,-1] for _ in range(V+1)] #누적값 1,2 번쨰로 큰 거 저장

for i in range(1,V+1):
    l = list(map(int, input().split()))
    for idx in range(1,len(l)-1,2):
        tree[l[0]].append([l[idx],l[idx+1]])
    
visited = [0 for _ in range(V+1)]

def DFS(node):
    
    visited[node]=1
    if node!=1 and len(tree[node])==1:
        dp[node] = [0,0]
        return 0
    
    for child, dist in tree[node]:
        if visited[child] :
            continue
        
        f = DFS(child)
        tmp = f + dist 
        
        if tmp > dp[node][1]:
            
            if tmp>dp[node][0]:
                dp[node][0],dp[node][1] = tmp, dp[node][0]

            else:
                dp[node][1] = tmp

    return dp[node][0]
DFS(1)

print(dp)
sol = 0
for i in range(1,V+1):
    if dp[i][1]==-1:
        sol = max(dp[i][0], sol)
    else:
        sol = max(dp[i][0]+dp[i][1], sol)
        
print(sol)    

