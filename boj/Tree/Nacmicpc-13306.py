#트리 #offline query
#부모 리스트 저장해두고 다시 갱신하는 방식으로 풀려고 했다.
#거꾸로 union find 해야되는 문제였다. 미친문제네
def find(u):
    if p[u]<0:
        return u
    p[u] = find(p[u])
    return p[u]
    
N,Q = map(int, input().split())
p= [-1 for _ in range(N+1)] #0번은 빈칸, 1번 노드는 루트
save=[ -1 for _ in range(N+1)]
for i in range(N-1):
    a= int(input())
    p[i+2] = a
    save[i+2] = a

for i in range(N-1+Q):
    q = list(map(int, input().split())) 
    if len(q)==3:
        c,d = q[1],q[2]

        save=p[:]
        
        if find(c)==find(d):
            print('YES')
        else:
            print('NO')
        
        p = save[:]
        
    elif len(q)==2:
        b=q[1]
        
        p[b]=-1
        save[b]=-1