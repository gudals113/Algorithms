import sys
sys.setrecursionlimit(10**5)

def find(a) :
    if p[a] < 0 :
        return a
    p[a]= find(p[a])
    return p[a]
    
def union(a,b) :
    a= find(a)
    b= find(b)
    if a==b :
        return
    
    else:
        if abs(p[a]) >= abs(p[b]):
            p[a] += p[b]
            p[b] =a

        else:
            p[b] += p[a]
            p[a] =b
            
N, M = map(int, input().split())
p= [ -1 for _ in range(N+1)]
for _ in range(M):
    f, a, b = map(int,input().split())
    
    if f ==0 :
        union(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        
        else:
            print('NO')