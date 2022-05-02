#행성 터널 MST
#프림
#정렬해서 크루스칼 사용해야되나
def find(u) :
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]

def union(u,v) : #v가 루트가 된다.
    u,v = find(u),find(v)
    if u==v:
        return
    
    if u < v:
        p[v]=u
    else:
        p[u]=v

N = int(input())
G=[]
p=[-1 for _ in range(N+1)]
for i in range(N):
    G.append( [i]+list(map(int, input().split())) )

#idx, x,y,z 
Gx=sorted(G, key=lambda x :x[1])
Gy=sorted(G, key=lambda x :x[2])
Gz=sorted(G, key=lambda x :x[3])

E=[]
for i in range(1,N):
    u, ux, _, _ =Gx[i-1] 
    v, vx, _, _ =Gx[i]
    E.append([ u,v, abs(ux-vx)])

for i in range(1,N):
    u, _, uy, _ =Gy[i-1] 
    v, _, vy, _ =Gy[i]
    E.append([ u,v, abs(uy-vy)])

for i in range(1,N):
    u, _, _, uz =Gz[i-1] 
    v, _, _, vz =Gz[i]
    E.append([ u,v, abs(uz-vz)])

E.sort(key=lambda x : x[2])
sol=0
count=0
for i in range(len(E)):
    if count == N-1:
        break
    u,v,cost=E[i]
    
    if find(u)!=find(v):
        union(u,v)
        sol+=cost
        count+=1
print(sol)