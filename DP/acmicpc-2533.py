#tree+dp
#백준 2533번 사회망 서비스
#pypy3로 풀면 메모리 초과 발생, 예전과 메모리 기준이 달라진 듯
import sys
sys.setrecursionlimit(10**9)
N=int(sys.stdin.readline())
tree=[[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

dp=[[0,0] for _ in range(N+1)]
visited=[0]*(N+1)

def DFS(node):
    visited[node]=1
    dp[node][1]=1
    for v in tree[node]:
        if visited[v]==0:
            DFS(v)
            dp[node][1] +=  min(dp[v][0], dp[v][1])
            dp[node][0] +=  dp[v][1]
DFS(1)
print(min(dp[1][0], dp[1][1]) )


