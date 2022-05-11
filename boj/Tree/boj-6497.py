#전력난 MST, krusckal, 220506
while True:
    M,N = map(int,input().split())
    if M==0 and N == 0:
        break
    
    G=[]
    for _ in range(N):
        G.append(list(map(int, input().split()))) 
    


    G.sort(key=lambda x:x[2])
    p = [-1 for _ in range(M)]

    def find(u):
        if p[u]<0 :
            return u
        
        p[u] = find(p[u])
        return p[u]

    def union(u,v):
        u=find(u)
        v=find(v)
        
        if u==v:
            return
        
        if u < v :
            p[v] = u
        else:
            p[u] = v

    sol = 0
    for u,v,cost in G :
        if find(u) != find(v) :
            union(u,v)
        else:
            sol+=cost
            
    print(sol) 