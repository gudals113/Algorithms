#MST 게임
#크루스칼
def find(u):
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v):
    u, v = find(u), find(v)
    if u==v:
        return
    
    if u<=v :
        p[v]=u
    else:
        p[u]=v
    
N, M, K = map(int,input().split())
G=[]
for i in range(1,M+1):
    x,y=map(int,input().split())
    G.append([x,y,i])
G.sort(key=lambda x:x[2])
G.append([0,0,0])

sol=[]
for k in range(K):
    
    p=[-1 for _ in range(N+1)]
    toDel=-1
    count=0
    score = 0
    isMST= False
    for i in range(len(G)):
        if count == N-1 :
            isMST=True
            break
        
        u,v, cost = G[i]
        
        if find(u) != find(v):
            union(u,v)
            score+=cost
            count+=1
            
            if toDel==-1: #가장 처음 등장하는 것
                toDel=i
    
    if isMST==True:
        del G[toDel]
        sol.append(score)
    else:
        sol+=[0 for _ in range(K-k)]
        break
    
print(*sol)