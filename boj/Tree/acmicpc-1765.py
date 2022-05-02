#닭싸움 팀 정하기union find
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
    
    if abs(p[u]) >= abs(p[v]):
        p[u]+=p[v]
        p[v]=u
    
    else:
        p[v]+=p[u]
        p[u]=v
    
N= int(input())
p = [-1 for _ in range(N+1)]
e = [[] for _ in range(N+1)]
M = int(input())

for i in range(M):
    r, a, b = input().split()
    a,b = int(a), int(b)
    if r=='F' :
        union(a,b)
    else:
        e[a].append(b)
        e[b].append(a)

for i in range(1, N+1):        #각 학생들의 원수 배열을 탐색하며, 원수가 2명 이상이면 그 원수끼리 모두 팀으로 만들기 
    if len(e[i]) > 1:
        for j in range(1, len(e[i])):
            union(e[i][j-1], e[i][j])
    
sol=0
for i in range(1, N+1):
    if p[i]<0:
        sol+=1
print(sol)