#보석줍기 bitmasking
N,M,K= map( int, input().split() )
path=[[0 for _ in range(N+1)] for _ in range(N+1)]
diamond=[0 for _ in range(N+1)]
for _ in range(K):
    l = int(input())
    diamond[l]=1
for _ in range(M):
    a,b,c = map( int, input().split() )
    path[a][b]=c
    path[b][a]=c

dp=[ [ [0 for _ in range(1<<100)] for _ in range(2) ] for _ in range(101) ]
ALL_VISITED=(1<<101) - 1
def finding(last, take, visited):
    if visited== ALL_VISITED :
        return 