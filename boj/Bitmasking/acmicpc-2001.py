#보석줍기 bitmasking
from collections import deque

def bitCount(bit):
    count=0
    while bit>0:
        count+= 0b1 & bit
        bit = bit>>1
    return count

N,M,K= map( int, input().split() )
path=[[]for _ in range(N+1)]
diamond=[]

for _ in range(K):
    l = int(input())
    diamond.append(l)
for _ in range(M):
    a,b,c = map( int, input().split() )
    path[a].append((b,c))
    path[b].append((a,c))


# visited=[위치][보석]
visited=[ [-1 for _ in range(1<<K)] for _ in range(N+1) ] # 1 000 000 000 000 00
visited[1][0]=0
tmp=0

q=deque([[1,0]])
while (q):
    last,have = q.popleft()
    num=bitCount(have)# 현재 보석 가지고 있는 개수
  
    for island, weight in path[last]: # last에서 모든 아일랜드로 돌려보자
        if weight >= num and weight>0 : 
                    
            if visited[island][have]==-1:
                visited[island][have]=0
                q.append([island, have])
                
            if island in diamond :
                newhave=have|1<<(diamond.index(island))
                if visited[island][newhave]==-1:           
                    # have=newhave 이거 때문에 계속 오류 발생했다!!
                    visited[island][newhave]=0
                    q.append([island, newhave])
            
            
print(max(bitCount(i) for i in range(1<<K) if visited[1][i]==0))