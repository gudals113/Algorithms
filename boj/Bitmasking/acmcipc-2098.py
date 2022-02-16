#TSP 외판원 순회 
import sys
limit_number = 150000
sys.setrecursionlimit(limit_number)


N=int(input())
path=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    line= list( map ( int, input().split() ) )
    for j in range(N):
        path[i][j]= line[j]


dp=[[0 for _ in range(1<<N)] for _ in range(N)] #dp[N][1<<N]

VISITED_COMPLETE = (1<<N) -1 # 모든 도시 1인 경우
INF= float('inf')

def visiting(last, visited):
    
    if visited==VISITED_COMPLETE :
        return path[last][0] or INF

    if dp[last][visited]!=0:
        return dp[last][visited]

    tmp=INF
    for i in range(N):
        if visited & (1<<i) ==0 and path[last][i]!=0: #방문하지 않은 마을 & path 가 존재
            tmp= min ( tmp, visiting(i, visited | 1<<i ) + path[last][i] )

    dp[last][visited]=tmp
    return tmp

sol = visiting(0, 1<<0 )
print(sol)

