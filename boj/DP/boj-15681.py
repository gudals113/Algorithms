#트리와 쿼리 (tree + dp ) 220503
#dp[node] = 1 이후에 
#if len(tree[node]==1) : return 했는데 틀렸다. 반례 무엇이지? 
#반례 = > 노드 2개인 경우! if len(tree[node]==1) and node!=R : return 이렇게 하면 풀린다!!

import sys
sys.setrecursionlimit(10**4)
N, R, Q = map(int,input().split())

tree = [ [] for _ in range(N+1)  ]
for _ in range(N-1):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [-1 for _ in range(N+1)]

def find(node):
     
    dp[node] = 1
    
    for next in tree[node] :
        if dp[next] == -1 :
            dp[node] += find(next)
    
    return dp[node]



find(R) 
sol = []
for _ in range(Q) :
    U = int(input())
    sol.append(dp[U])
    
for i in range(Q):
    print(sol[i])
    
