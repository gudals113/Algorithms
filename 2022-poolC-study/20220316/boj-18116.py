import sys
input = sys.stdin.readline
def find(u) :
    if p[u]<0:
        return u
    
    p[u] =find(p[u])
    return p[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v:
        return True
    
    
    if abs(p[u]) > abs(p[v]) :
        p[u]+=p[v]
        p[v]=u
    else:
        p[v]+=p[u]
        p[u]=v          
    return False

p = [-1 for _ in range(10**6+1)]
# count= [1 for _ in range(10**6+1)]
N = int(input())

for _ in range(N):
    line = list(input().split())
    
    if len(line)==3:
        
        if union(int(line[1]), int(line[2])) == False:
            pass

    else:
        parent = find(int(line[1]))
        print(abs(p[parent]))