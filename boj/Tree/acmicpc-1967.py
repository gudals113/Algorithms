#여행 가자 union find
N = int(input())
M = int(input())

path= [ [] for _ in range(N+1) ] 
p=[-1 for _ in range(N+1)]

for i in range(N): 
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j]==1:
            path[i+1].append(j+1)
            path[j+1].append(i+1)
                                        
plan = list(map(int, input().split()))

def find(u):
    if p[u] <0 : 
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) :
    u=find(u)
    v=find(v)
    if u==v :
        return    
    p[u]=v

for i in range(1, N+1):
    for n in path[i]:
        union(i,n)
            
tmp = find(plan[0]) #이렇게 말고 방법이 있나?
sol = 'YES'
for i in range(1, M) :
    if tmp != find(plan[i]) :
        sol='NO'
        break
print(sol)
    
    