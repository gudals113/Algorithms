#친구 네트워크 (union find)
def find(u):
    if type(dict[u]) == int:
        return u
    
    dict[u] = find(dict[u])
    return dict[u]

def union(u,v):
    u,v = find(u), find(v)
    if u==v:
        return u
    
    if abs(dict[u]) >= abs(dict[v]):
        dict[u]+=dict[v]
        dict[v]=u
        return u
    else:
        dict[v]+=dict[u]
        dict[u]=v
        return v
    
T= int(input())
for _ in range(T):
    F = int(input())
    dict={}
    for i in range(F):
        
        A, B = input().split()
        
        if A not in dict:
            dict[A] =-1
        if B not in dict:
            dict[B] =-1
        
        root =union(A,B)
        print(abs(dict[root]))
        
    