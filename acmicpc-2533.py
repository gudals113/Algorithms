N=int(input)
tree=[[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp=[[0,0] for _ in range(N+1)]

for i in range(1,N+1):
    node=tree[i]

    dp[node][0]=
    dp[node][1]

